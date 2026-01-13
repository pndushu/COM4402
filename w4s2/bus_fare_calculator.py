def get_fare(age: int, is_peak: bool) -> float:
    if not isinstance(age, int) or not isinstance(is_peak, bool):
        raise TypeError
    if age < 0:
        raise ValueError

    fare = 1.25 if age < 16 else 1.00 if age >= 65 else 2.50
    return fare if is_peak else fare * 0.8
