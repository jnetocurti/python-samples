import csv
from urllib import request


def read(path):
    file = open(path)
    data = file.read()
    file.close()

    for line in data.splitlines():
        print('{0}  {1}  {2}'.format(*line.split(';')))


def read_streams(path):
    file = open(path)
    for line in file:
        print('{0}  {1}  {2}'.format(*line.split(';')))

    file.close()


def read_try_finally(path):
    try:
        file = open(path)
        for line in file:
            print('{0}  {1}  {2}'.format(*line.split(';')))

    finally:
        file.close()


def read_with_block(path):
    with open(path) as file:
        for line in file:
            print('{0}  {1}  {2}'.format(*line.split(';')))


def read_csv_module(path):
    with open(path) as file:
        for line in csv.reader(file, delimiter=';'):
            print('{0}  {1}  {2}'.format(*line))


def read_and_write(path, out):
    with open(path) as file:
        with open(out, 'w') as output_file:
            for line in csv.reader(file, delimiter=';'):
                print(*line, file=output_file)


def read_from_url(url):
    with request.urlopen(url) as file:
        data = file.read().decode('UTF-8')

        for line in csv.reader(data.splitlines(), delimiter=';'):
            print('{0}  {1}  {2}'.format(*line))
