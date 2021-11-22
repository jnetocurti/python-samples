from calendar import mdays, month_name
from functools import reduce


def zip_months_and_days():
    ziped_months = zip(month_name, mdays)
    return list(filter(lambda m: len(m[0]) > 0, ziped_months))


def filter_months_with_31_days():
    months = zip_months_and_days()
    return list(filter(lambda m: m[1] > 30, months))


def map_to_only_month_names():
    months = zip_months_and_days()
    return list(map(lambda m: m[0], months))


def reduce_year_months_to_total_days():
    months = zip_months_and_days()
    return reduce(lambda a, c: a + c[1], months, 0)


def reduce_to_month_with_smaller_name():
    months = map(lambda m: m[0], zip_months_and_days())
    return reduce(lambda a, c: a if len(a) < len(c) else c, months)
