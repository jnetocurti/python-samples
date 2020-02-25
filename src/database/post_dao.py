from .post import Post
from .connection import connection
from mysql.connector.errors import ProgrammingError


class PostDao():

    def save(self, post):
        query = "INSERT INTO posts(subject, content) VALUES (%s, %s)"
        with connection() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, (post.subject, post.content))
                conn.commit()
            except ProgrammingError as error:
                print(f"Error to save post: {error}")
                raise error
            else:
                id = cursor.lastrowid
                return Post(id=id, subject=post.subject, content=post.content)

    def bulk_save(self, posts):
        query = "INSERT INTO posts(subject, content) VALUES (%s, %s)"
        with connection() as conn:
            try:
                args = tuple(
                    [(p.subject, p.content) for p in posts]
                )
                cursor = conn.cursor()
                cursor.executemany(query, args)
                conn.commit()
            except ProgrammingError as error:
                print(f"Error to save post: {error}")
                raise error
            else:
                return cursor.rowcount

    def update(self):
        pass

    def delete(self):
        pass

    def find_by_id(self, id):
        query = "SELECT * FROM posts WHERE id = %s"
        with connection() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, (id,))
            except ProgrammingError as error:
                print(f"Error to search posts: {error}")
                raise error
            else:
                result = cursor.fetchone()
                return Post(
                    id=result[0],
                    subject=result[1],
                    content=result[2]
                )

    def find_all(self):
        with connection() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM posts")
            except ProgrammingError as error:
                print(f"Error to search posts: {error}")
                raise error
            else:
                return [Post(id=p[0], subject=p[1], content=p[2])
                        for p in cursor.fetchall()]
