from logic import calculate_split

def test_basic_calculation():
    """Проверяем корректный расчёт с чаевыми."""
    result = calculate_split(1000.0, 10.0, 2)
    assert result["tip_amount"] == 100.0
    assert result["total"] == 1100.0
    assert result["per_person"] == 550.0

def test_zero_tip():
    """Проверяем расчёт без чаевых."""
    result = calculate_split(500.0, 0.0, 5)
    assert result["tip_amount"] == 0.0
    assert result["total"] == 500.0
    assert result["per_person"] == 100.0

def test_rounding():
    """Проверяем округление до 2 знаков."""
    result = calculate_split(100.0, 15.0, 3)
    assert result["per_person"] == 38.33
