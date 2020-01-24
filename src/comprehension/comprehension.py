

def get_from_simple_list_comprehension(start=0, end=10):
    return [i for i in range(start, end)]


def get_from_conditional_list_comprehension(start=0, end=10):
    return [i for i in range(start, end) if i % 2 == 0]


def get_from_list_comprehension_merge_dicts(list_one, list_two):
    return [dict(a, **b) for b in list_two for a in list_one
            if a.get('id') == b.get('id')]


def get_from_flat_map_simple_list_comprehension(list):
    return [item for sublist in list for item in sublist]


def get_from_flat_map_dict_list_comprehension(list):
    return [b for a in list for b in a['activities']]


def get_from_simple_generator(start=0, end=10):
    return (i for i in range(start, end))


def get_from_conditional_generator(start=0, end=10):
    return (i for i in range(start, end) if i % 2 == 0)


def get_from_simple_dict_comprehension(list):
    return {list.index(value): value for value in list}


def get_from_conditional_dict_comprehension(list):
    return {list.index(value): value for value in list if value == 'play'}


def get_from_dict_comprehension_merge_dicts(list_one, list_two):
    return {a.get('id'): dict(a, **b) for b in list_two for a in list_one
            if a.get('id') == b.get('id')}
