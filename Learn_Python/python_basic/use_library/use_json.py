import json


def dict_to_json():
    dict1 = {'name': 'tom', 'age': 20, 'sex': 'male'}
    print(dict1)
    jsons = json.dumps(dict1)
    print(jsons)
    print(type(jsons))


def json_to_dict():
    jsons = '{"name": "tony", "age": 28, "sex": "male", "phone": "123456", "email": "loadkernel@126.com"}'
    dict1 = json.loads(jsons)
    print(dict1)
    print(type(dict1))


def dict_to_json_write_file():
    dict1 = {'name': 'tom', 'age': 10, 'sex': 'male'}
    print(dict1)
    with open('test2.json', 'w') as f:
        json.dump(dict1, f)


def json_file_to_dict():
    with open('test.json', 'r') as f:
        dict1 = json.load(f)
        print(dict1)
        print(type(dict1))


if __name__ == '__main__':
    dict_to_json()
    json_to_dict()
    # dict_to_json_write_file()
    # json_file_to_dict()
