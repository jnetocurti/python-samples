from .post import Post
from .connection import connection
from mysql.connector.errors import ProgrammingError


class PostDao():

    def save(self, post):
        query = "INSERT INTO posts(subject, content) values (%s, %s)"
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
                return Post(post.subject, post.content, id)

    def bulk_save(self, posts):
        query = "INSERT INTO posts(subject, content) values (%s, %s)"
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

    def find(self):
        pass

    def find_all(self):
        pass
