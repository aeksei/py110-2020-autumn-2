import json
import pickle

PICKLE_FILENAME = 'tmp.pickle'


def to_json_string(obj, indent=4):
    json_str = json.dumps(obj, indent=indent)
    return json_str


def to_pickle_file(obj, filename):
    if not filename.endswith('.pickle'):
        filename += '.pickle'
    with open(filename, 'wb') as pickle_file:
        pickle.dump(obj, pickle_file)


def to_json_file(obj, filename, indent=1, separators=None):
    # todo separators для записи в одну строку
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(obj, json_file, indent=indent, separators=separators)


if __name__ == '__main__':
    dict_json = {
        1: 1,
        "2": 5,
        "str": [122, 0x123, 123],
        "tuple": (1, 2, 3),
        "d": {1: 5},
    }
    # print(to_json_string(dict_json))

    to_pickle_file(dict_json, PICKLE_FILENAME)

    dict_pickle = {
        1: 1,
        "2": 5,
        (5, 7): "test",
        "str": [122, 0x123, 123],
        "tuple": (1, 2, 3),
        "d": {1: 5},
        "func": to_json_string
    }
    # todo попробовать записать dict_pickle c помощью to_json_string
    # to_pickle_file(dict_pickle, PICKLE_FILENAME)
    # to_pickle_file(dict_pickle, 'tmp1')

    to_json_file(dict_json, 'tmp.json', indent=4)
