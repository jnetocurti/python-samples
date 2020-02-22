import pytest
from src.database.post import Post
from src.database.post_dao import PostDao
from src.database.connection import connection

post_dao = PostDao()


@pytest.fixture(autouse=True)
def init():
    with connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            create table if not exists posts(
                id int auto_increment primary key,
                subject varchar(50) not null,
                content varchar(200) not null
            )""")
        yield
        cursor.execute("drop table posts")


def test_insert():
    post = post_dao.save(
        Post("Test subject", "Test content")
    )
    assert 1 == post.id


def test_bulk_save():
    row_count = post_dao.bulk_save([
        Post("Test subject 1", "Test content 1"),
        Post("Test subject 2", "Test content 2"),
        Post("Test subject 3", "Test content 3")
    ])
    assert 3 == row_count
