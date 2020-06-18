from flask import Flask, jsonify
from libs.cases import get_covid_cases
from libs.timedate import getDate


app = Flask(__name__)


@app.route("/api/v1", methods=["GET"])
@app.route("/api/v1/<date>", methods=["GET"])
def index(date=None):
    body_data = requests.json

    print(body_data)
    if date is None:
        query_date = requests.args.get('date')
        if query_date is not None:
            d = query_date
        else:
            d = getDate()
        cases = get_covid_cases(d)
    else:
        cases = get_covid_cases(date)

    return jsonify({"total_cases": cases})


if __name__ == "__main__":
    app.run(debug=True)
