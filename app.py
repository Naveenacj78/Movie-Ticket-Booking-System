from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)
from flask import send_file
from reportlab.pdfgen import canvas
import os
import os
from werkzeug.utils import secure_filename
from reportlab.pdfgen import canvas

from database.database import (
    create_tables,
    create_default_admin,
    get_connection
)

from models.user import User
from models.admin import Admin
from models.movie import Movie
from models.booking import Booking
from models.seat import Seat

from services.export_service import ExportService

app = Flask(__name__)

app.secret_key = "movie_booking_secret_key"

create_tables()
create_default_admin()


# ======================
# HOME
# ======================

@app.route("/")
def home():
    return render_template("index.html")


# ======================
# USER REGISTER
# ======================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        User.register(
            request.form["name"],
            request.form["email"],
            request.form["password"]
        )

        flash(
            "Registration Successful",
            "success"
        )

        return redirect(
            url_for("login")
        )

    return render_template(
        "register.html"
    )


# ======================
# USER LOGIN
# ======================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        user = User.login(
            request.form["email"],
            request.form["password"]
        )

        if user:

            session["user_id"] = user[0]
            session["user_name"] = user[1]

            return redirect(
                url_for(
                    "user_dashboard"
                )
            )

        flash(
            "Invalid Credentials",
            "danger"
        )

    return render_template(
        "login.html"
    )


# ======================
# ADMIN LOGIN
# ======================

@app.route(
    "/admin-login",
    methods=["GET", "POST"]
)
def admin_login():

    if request.method == "POST":

        admin = Admin.login(
            request.form["username"],
            request.form["password"]
        )

        if admin:

            session["admin"] = True

            return redirect(
                url_for(
                    "admin_dashboard"
                )
            )

        flash(
            "Invalid Admin Login",
            "danger"
        )

    return render_template(
        "admin_login.html"
    )


# ======================
# USER DASHBOARD
# ======================

@app.route("/user-dashboard")
def user_dashboard():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    return render_template(
        "user_dashboard.html",
        username=session["user_name"]
    )


# ======================
# ADMIN DASHBOARD
# ======================

@app.route("/admin-dashboard")
def admin_dashboard():

    if "admin" not in session:

        return redirect(
            url_for(
                "admin_login"
            )
        )

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM Movies"
    )
    total_movies = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM Users"
    )
    total_users = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM Bookings"
    )
    total_bookings = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "admin_dashboard.html",
        total_movies=total_movies,
        total_users=total_users,
        total_bookings=total_bookings
    )


# ======================
# MOVIES
# ======================

@app.route("/movies")
def movies():

    search = request.args.get(
        "search"
    )

    if search:
        movies = Movie.search_movie(
            search
        )
    else:
        movies = Movie.get_all_movies()

    return render_template(
        "movies.html",
        movies=movies
    )


# ======================
# ADD MOVIE
# ======================

@app.route(
    "/add-movie",
    methods=["GET", "POST"]
)
def add_movie():

    if "admin" not in session:
        return redirect(
            url_for(
                "admin_login"
            )
        )

    if request.method == "POST":

        title = request.form["title"]
        genre = request.form["genre"]
        show_time = request.form["show_time"]

        total_seats = int(
            request.form["total_seats"]
        )

        poster = request.files["poster"]

        filename = None

        if poster and poster.filename:

            os.makedirs(
                "static/posters",
                exist_ok=True
            )

            filename = secure_filename(
                poster.filename
            )

            poster.save(
                os.path.join(
                    "static/posters",
                    filename
                )
            )

        movie_id = Movie.add_movie(
            title,
            genre,
            show_time,
            total_seats,
            filename
        )

        Seat.create_seats(
            movie_id
        )

        flash(
            "Movie Added",
            "success"
        )

        return redirect(
            url_for("movies")
        )

    return render_template(
        "add_movie.html"
    )


# ======================
# EDIT MOVIE
# ======================

@app.route(
    "/edit-movie/<int:movie_id>",
    methods=["GET", "POST"]
)
def edit_movie(movie_id):

    movie = Movie.get_movie(
        movie_id
    )

    if request.method == "POST":

        Movie.update_movie(
            movie_id,
            request.form["title"],
            request.form["genre"],
            request.form["show_time"]
        )

        flash(
            "Movie Updated",
            "success"
        )

        return redirect(
            url_for("movies")
        )

    return render_template(
        "edit_movie.html",
        movie=movie
    )


# ======================
# DELETE MOVIE
# ======================

@app.route(
    "/delete-movie/<int:movie_id>"
)
def delete_movie(movie_id):

    Movie.delete_movie(
        movie_id
    )

    flash(
        "Movie Deleted",
        "danger"
    )

    return redirect(
        url_for("movies")
    )


# ======================
# BOOK MOVIE
# ======================

@app.route(
    "/book-movie/<int:movie_id>",
    methods=["GET", "POST"]
)
def book_movie(movie_id):

    movie = Movie.get_movie(
        movie_id
    )

    seats = Seat.get_available_seats(
        movie_id
    )

    if request.method == "POST":

        seat_number = request.form[
            "seat_number"
        ]

        Booking.create_booking(
            session["user_id"],
            movie_id,
            seat_number
        )

        Seat.book_seat(
            movie_id,
            seat_number
        )

        flash(
            "Booking Successful",
            "success"
        )

        return redirect(
            url_for("bookings")
        )

    return render_template(
        "select_seat.html",
        movie=movie,
        seats=seats
    )


# ======================
# BOOKINGS
# ======================

@app.route("/bookings")
def bookings():

    bookings = (
        Booking.get_user_bookings(
            session["user_id"]
        )
    )

    return render_template(
        "bookings.html",
        bookings=bookings
    )


# ======================
# CANCEL BOOKING
# ======================

@app.route(
    "/cancel-booking/<int:booking_id>"
)
def cancel_booking(booking_id):

    result = Booking.cancel_booking(
        booking_id
    )

    if result:

        Seat.free_seat(
            result[0],
            result[1]
        )

    return redirect(
        url_for("bookings")
    )


# ======================
# RECEIPT
# ======================
@app.route("/generate-receipt/<int:booking_id>")
def generate_receipt(booking_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        b.booking_id,
        u.name,
        m.title,
        m.genre,
        m.show_time,
        b.seat_number,
        b.booking_time
    FROM Bookings b
    JOIN Users u
        ON b.user_id = u.user_id
    JOIN Movies m
        ON b.movie_id = m.movie_id
    WHERE b.booking_id = ?
    """, (booking_id,))

    row = cursor.fetchone()

    conn.close()

    if not row:
        return "Receipt Not Found"

    receipt = {
        "booking_id": row[0],
        "user_name": row[1],
        "movie_name": row[2],
        "genre": row[3],
        "show_time": row[4],
        "seat_number": row[5],
        "booking_time": row[6]
    }

    return render_template(
        "receipt.html",
        receipt=receipt
    )
# ======================
# REPORTS
# ======================

@app.route("/reports")
def reports():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
    m.title,
    COUNT(b.booking_id)

    FROM Movies m

    LEFT JOIN Bookings b
    ON m.movie_id=b.movie_id

    GROUP BY m.title
    """)

    report = cursor.fetchall()

    conn.close()

    return render_template(
        "reports.html",
        report=report
    )


# ======================
# ANALYTICS
# ======================

@app.route("/analytics")
def analytics():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM Bookings"
    )

    bookings = cursor.fetchone()[0]

    revenue = bookings * 200

    conn.close()

    return render_template(
        "analytics.html",
        revenue=revenue,
        bookings=bookings
    )


# ======================
# EXPORTS
# ======================

@app.route("/export-bookings")
def export_bookings():

    ExportService.export_bookings_csv()

    return redirect(
        url_for(
            "admin_dashboard"
        )
    )


@app.route("/export-sales")
def export_sales():

    ExportService.export_sales_csv()

    return redirect(
        url_for(
            "admin_dashboard"
        )
    )


# ======================
# LOGOUT
# ======================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("home")
    )

@app.route("/receipt-pdf/<int:booking_id>")
def receipt_pdf(booking_id):

    os.makedirs(
        "receipts",
        exist_ok=True
    )

    pdf_file = (
        f"receipts/receipt_{booking_id}.pdf"
    )

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        b.booking_id,
        u.name,
        m.title,
        m.genre,
        m.show_time,
        b.seat_number,
        b.booking_time
    FROM Bookings b
    JOIN Users u
        ON b.user_id = u.user_id
    JOIN Movies m
        ON b.movie_id = m.movie_id
    WHERE b.booking_id = ?
    """, (booking_id,))

    row = cursor.fetchone()

    conn.close()

    if not row:
        return "Receipt Not Found"

    pdf = canvas.Canvas(pdf_file)

    pdf.drawString(
        100,
        800,
        "MOVIE TICKET RECEIPT"
    )

    pdf.drawString(
        100,
        760,
        f"Booking ID: {row[0]}"
    )

    pdf.drawString(
        100,
        730,
        f"Customer: {row[1]}"
    )

    pdf.drawString(
        100,
        700,
        f"Movie: {row[2]}"
    )

    pdf.drawString(
        100,
        670,
        f"Genre: {row[3]}"
    )

    pdf.drawString(
        100,
        640,
        f"Show Time: {row[4]}"
    )

    pdf.drawString(
        100,
        610,
        f"Seat Number: {row[5]}"
    )

    pdf.drawString(
        100,
        580,
        f"Booking Time: {row[6]}"
    )

    pdf.drawString(
        100,
        550,
        "Status: CONFIRMED"
    )

    pdf.save()

    return send_file(
        pdf_file,
        as_attachment=True
    )

# ======================
# START APP
# ======================

if __name__ == "__main__":
    app.run(debug=True)