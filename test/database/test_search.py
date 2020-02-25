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


def find_by_id():
    post = post_dao.find_by_id(2)
    assert 2 == post.id
    assert "Test subject 2" == post.subject
    assert "Test content 2" == post.content


def test_find_all():
    records = post_dao.find_all()
    assert 3 == len(records)
    assert "Test content 1" == records[0].content
    assert "Test content 2" == records[1].content
    assert "Test content 3" == records[2].content
