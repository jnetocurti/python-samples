from io import StringIO
from os import path

from mock import patch
from src.files import files

INPUT_FILE_PATH = "assets/fiis.csv"
OUTPUT_FILE_PATH = "assets/fiis.txt"
FILE_URL = r"https://raw.githubusercontent.com/jnetocurti/python-samples/master/assets/fiis.csv"  # noqa

STDOUT_RESULT = (
    "CÓDIGO DO FUNDO  SETOR  PREÇO ATUAL\n" +
    "BBRC11  Outros  R$ 145,99\n" +
    "FLMA11  Híbrido  R$ 4,66\n" +
    "FOFT11  Títulos e Val. Mob.  R$ 123,00\n" +
    "HSML11  Shoppings  R$ 124,90\n" +
    "SDIP11  Lajes Corporativas  R$ 113,05\n" +
    "XPLG11  Logística  R$ 139,25\n")


@patch("sys.stdout", new_callable=StringIO)
def test_read(mock_stdout):
    files.read(INPUT_FILE_PATH)
    assert mock_stdout.getvalue() == STDOUT_RESULT


@patch("sys.stdout", new_callable=StringIO)
def test_read_streams(mock_stdout):
    files.read_streams(INPUT_FILE_PATH)
    assert mock_stdout.getvalue() == STDOUT_RESULT


@patch("sys.stdout", new_callable=StringIO)
def test_read_try_finally(mock_stdout):
    files.read_try_finally(INPUT_FILE_PATH)
    assert mock_stdout.getvalue() == STDOUT_RESULT


@patch("sys.stdout", new_callable=StringIO)
def test_read_with_block(mock_stdout):
    files.read_with_block(INPUT_FILE_PATH)
    assert mock_stdout.getvalue() == STDOUT_RESULT


@patch("sys.stdout", new_callable=StringIO)
def test_read_csv_module(mock_stdout):
    files.read_csv_module(INPUT_FILE_PATH)
    assert mock_stdout.getvalue() == STDOUT_RESULT


def test_read_and_write():
    files.read_and_write(INPUT_FILE_PATH, OUTPUT_FILE_PATH)
    assert path.exists(OUTPUT_FILE_PATH)


@patch("sys.stdout", new_callable=StringIO)
def test_read_from_url(mock_stdout):
    files.read_from_url(FILE_URL)
    assert mock_stdout.getvalue() == STDOUT_RESULT
