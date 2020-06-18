from .reader import get_csv_reader
from .countries import countries

base_url = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/"


def get_covid_cases(date):
    csv_url = base_url + date + ".csv"

    covid_cases = []
    reader = get_csv_reader(csv_url)

    for row in reader:
        if row[3] in countries:
            covid_cases.append(
                {
                    "Country": row[3],
                    "Confirmed": row[7],
                    "Deaths": row[8],
                    "Recovered": row[9],
                    "Active": row[10],
                }
            )

    return covid_cases
