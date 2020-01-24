from src.comprehension import comprehension


def test_get_from_simple_list_comprehension():
    assert 10 == len(comprehension.get_from_simple_list_comprehension())
    assert 5 == len(comprehension.get_from_simple_list_comprehension(5, 10))


def test_get_from_conditional_list_comprehension():
    assert 5 == len(
        comprehension.get_from_conditional_list_comprehension())
    assert 2 == len(
        comprehension.get_from_conditional_list_comprehension(5, 10))


def test_get_from_list_comprehension_merge_dicts():
    descriptions = [
        {"id": 1, "description": "foo"},
        {"id": 3, "description": "bar"},
        {"id": 4, "description": "baz"}
    ]
    prices = [
        {"id": 1, "price": 5.45},
        {"id": 2, "price": 7.85},
        {"id": 3, "price": 15.23},
        {"id": 4, "price": 3.36}
    ]

    assert ([{"id": 1, "description": "foo", "price": 5.45},
             {"id": 3, "description": "bar", "price": 15.23},
             {"id": 4, "description": "baz", "price": 3.36}] == comprehension
            .get_from_list_comprehension_merge_dicts(descriptions, prices))


def test_get_from_flat_map_simple_list_comprehension():
    data = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]

    assert ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9] ==
            comprehension.get_from_flat_map_simple_list_comprehension(data))


def test_get_from_flat_map_dict_list_comprehension():
    data = [
        {
            "name": "foo",
            "activities": ['swim', 'play']
        },
        {
            "name": "bar",
            "activities": ['read', 'dance']
        }
    ]
    assert (['swim', 'play', 'read', 'dance'] ==
            comprehension.get_from_flat_map_dict_list_comprehension(data))


def test_get_from_simple_generator():
    assert ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9] == [
            a for a in comprehension.get_from_simple_generator()])

    result = comprehension.get_from_simple_generator(0, 3)
    assert 0 == next(result)
    assert 1 == next(result)
    assert 2 == next(result)
    assert None == next(result, None)


def test_get_from_conditional_generator():
    assert ([0, 2, 4, 6, 8] == [
            a for a in comprehension.get_from_conditional_generator()])

    result = comprehension.get_from_conditional_generator(0, 3)
    assert 0 == next(result)
    assert 2 == next(result)
    assert None == next(result, None)


def test_get_from_simple_dict_comprehension():
    data = ['swim', 'play', 'read', 'dance']

    assert ({0: 'swim', 1: 'play', 2: 'read', 3: 'dance'} ==
            comprehension.get_from_simple_dict_comprehension(data))


def test_get_from_conditional_dict_comprehension():
    data = ['swim', 'dance', 'read', 'play']

    assert ({3: 'play'} ==
            comprehension.get_from_conditional_dict_comprehension(data))


def test_get_from_dict_comprehension_merge_dicts():
    descriptions = [
        {"id": 1, "description": "foo"},
        {"id": 3, "description": "bar"},
        {"id": 4, "description": "baz"}
    ]
    prices = [
        {"id": 1, "price": 5.45},
        {"id": 2, "price": 7.85},
        {"id": 3, "price": 15.23},
        {"id": 4, "price": 3.36}
    ]

    assert ({
        1: {"id": 1, "description": "foo", "price": 5.45},
        3: {"id": 3, "description": "bar", "price": 15.23},
        4: {"id": 4, "description": "baz", "price": 3.36}
    } == comprehension
        .get_from_dict_comprehension_merge_dicts(descriptions, prices))
