from database.database import get_connection


class Movie:

    @staticmethod
    def add_movie(
            title,
            genre,
            show_time,
            total_seats,
            poster):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO Movies(
        title,
        genre,
        show_time,
        total_seats,
        available_seats,
        poster
        )
        VALUES(?,?,?,?,?,?)
        """, (
            title,
            genre,
            show_time,
            total_seats,
            total_seats,
            poster
        ))

        movie_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return movie_id

    @staticmethod
    def get_all_movies():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM Movies
        """)

        movies = cursor.fetchall()

        conn.close()

        return movies

    @staticmethod
    def get_movie(movie_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM Movies
        WHERE movie_id=?
        """, (movie_id,))

        movie = cursor.fetchone()

        conn.close()

        return movie

    @staticmethod
    def search_movie(keyword):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM Movies
        WHERE title LIKE ?
        """, ('%' + keyword + '%',))

        movies = cursor.fetchall()

        conn.close()

        return movies

    @staticmethod
    def update_movie(
            movie_id,
            title,
            genre,
            show_time):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE Movies
        SET
        title=?,
        genre=?,
        show_time=?
        WHERE movie_id=?
        """, (
            title,
            genre,
            show_time,
            movie_id
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def delete_movie(movie_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM Movies
        WHERE movie_id=?
        """, (movie_id,))

        conn.commit()
        conn.close()