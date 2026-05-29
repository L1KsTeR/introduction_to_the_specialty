def validate_input(data: dict) -> list[str]:
    errors = []
    bill = data.get("bill")
    tip = data.get("tip_percent")
    people = data.get("people")

    if bill is None or tip is None or people is None:
        return ["Отсутствуют обязательные поля: bill, tip_percent, people"]

    try:
        bill = float(bill)
        tip = float(tip)
        people = int(people)
    except (ValueError, TypeError):
        return ["Все значения должны быть числами"]

    if bill <= 0:
        errors.append("Сумма счёта должна быть больше 0")
    if tip < 0:
        errors.append("Процент чаевых не может быть отрицательным")
    if people < 1:
        errors.append("Количество людей должно быть ≥ 1")

    return errors
