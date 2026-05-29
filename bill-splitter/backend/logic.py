def calculate_split(bill: float, tip_percent: float, people: int) -> dict:
    tip_amount = bill * (tip_percent / 100)
    total = bill + tip_amount
    per_person = total / people

    return {
        "tip_amount": round(tip_amount, 2),
        "total": round(total, 2),
        "per_person": round(per_person, 2),
    }
