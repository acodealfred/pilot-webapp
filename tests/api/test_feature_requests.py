import pytest


@pytest.fixture(autouse=True)
def clear_requests():
    from app.main import feature_requests

    feature_requests.clear()
    yield
    feature_requests.clear()


def test_list_starts_empty(client):
    assert client.get("/api/feature-requests").json() == []


def test_create_and_list_newest_first(client):
    r = client.post("/api/feature-requests", json={"title": "A", "category": "UI"})
    assert r.status_code == 201
    client.post(
        "/api/feature-requests",
        json={"title": "B", "description": "more", "category": "Other"},
    )
    items = client.get("/api/feature-requests").json()
    assert [i["title"] for i in items] == ["B", "A"]
    assert items[0]["description"] == "more"
    assert items[1]["description"] == ""


@pytest.mark.parametrize("title", ["", "   "])
def test_blank_title_rejected(client, title):
    r = client.post("/api/feature-requests", json={"title": title, "category": "UI"})
    assert r.status_code == 422
    assert r.json()["detail"] == "Title is required"
    assert client.get("/api/feature-requests").json() == []


def test_unknown_category_rejected(client):
    r = client.post("/api/feature-requests", json={"title": "x", "category": "Security"})
    assert r.status_code == 422
