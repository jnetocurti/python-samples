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
        post_dao.bulk_save([
            Post(subject="Test subject 1", content="Test content 1"),
            Post(subject="Test subject 2", content="Test content 2"),
            Post(subject="Test subject 3", content="Test content 3")
        ])
        yield
        cursor.execute("drop table posts")


def test_update():
    assert 1 == post_dao.update(
        2,
        subject="Test subject 2 updated",
        content="Test content 2 updated"
    )
