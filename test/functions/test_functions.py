from src.functions.functions import zip_months_and_days, \
    filter_months_with_31_days, map_to_only_month_names, \
    reduce_year_months_to_total_days, reduce_to_month_with_smaller_name


def test_zip_months_and_days():
    assert [
        ('January', 31),
        ('February', 28),
        ('March', 31),
        ('April', 30),
        ('May', 31),
        ('June', 30),
        ('July', 31),
        ('August', 31),
        ('September', 30),
        ('October', 31),
        ('November', 30),
        ('December', 31)] == zip_months_and_days()


def test_filter_months_with_31_days():
    assert [
        ('January', 31),
        ('March', 31),
        ('May', 31),
        ('July', 31),
        ('August', 31),
        ('October', 31),
        ('December', 31)] == filter_months_with_31_days()


def test_map_to_only_month_names():
    assert [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'] == map_to_only_month_names()


def test_reduce_year_months_to_total_days():
    assert 365 == reduce_year_months_to_total_days()


def test_reduce_to_month_with_smaller_name():
    assert 'May' == reduce_to_month_with_smaller_name()
