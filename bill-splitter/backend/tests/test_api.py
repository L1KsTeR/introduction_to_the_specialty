import pytest

from app import app


@pytest.fixture
def client():
    """Создаёт тестовый клиент Flask."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_calculate_success(client):
    """Успешный запрос с корректными данными."""
    resp = client.post(
        "/api/calculate", json={"bill": 2000, "tip_percent": 15, "people": 4}
    )
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["per_person"] == 575.0


def test_calculate_invalid_negative_bill(client):
    """Отклонение отрицательной суммы счёта."""
    resp = client.post(
        "/api/calculate", json={"bill": -100, "tip_percent": 10, "people": 2}
    )
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_calculate_missing_fields(client):
    """Отклонение запроса без обязательных полей."""
    resp = client.post("/api/calculate", json={"bill": 100})
    assert resp.status_code == 400
