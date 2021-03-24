import json
import os

def readjson():
    with open(os.path.dirname(__file__) + '\\myjson.json', 'r', encoding='utf-8') as f:
        text = json.load(f)
        return text


def summ(a, b):
    return a + b


def diff(a, b):
    return a - b


def mul(a, b):
    return a * b


if __name__ == "__main__":
    print("Is main scrypt")
    readjson()
