import requests
import csv
from io import StringIO


def get_csv_reader(csv_url):
    res = requests.get(csv_url)
    data = res.content.decode("ascii", "ignore")

    return csv.reader(StringIO(data))
