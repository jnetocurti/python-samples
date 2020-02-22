from src.database.connection import connection


def test_connection():
    with connection() as conn:
        assert conn is not None
        assert conn.is_connected()
