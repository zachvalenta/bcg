import os

from app import app, db
from models import Pet


"""
CONF
"""


client = app.test_client()
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "test.db")


"""
XUNIT FIXTURES
"""


def setup_module():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path


def teardown_module():
    os.remove(db_path)


def setup_function():
    db.create_all()


def teardown_function():
    db.drop_all()


"""
TESTS
"""


def test_get_index_200():
    res = client.get("/")
    assert res.status_code == 200


def test_get_pet_price_by_id_200():
    db.session.add(
        Pet(
            species="dog",
            breed="golden_retriever",
            gender="female",
            name="lola",
            age=5,
            zip_code=10001,
        )
    )
    db.session.commit()
    res = client.get("/pet?id=1")
    assert res.status_code == 200


def test_get_pet_price_by_id_404_no_record():
    res = client.get("/pet?id=1")
    assert res.status_code == 404
