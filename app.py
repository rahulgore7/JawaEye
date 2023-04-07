import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sequence", methods=["POST"])
def sequence():
    num = float(request.form.get("number"))
    today = datetime.date.today()

    round_num = int(num // 10 * 10)
    percent = round_num * 0.02
    result = round(num + percent + 0.4, 2)

    sequence = [(today, num), (today + datetime.timedelta(days=1), result)]
    for i in range(2, 366):
        if i % 2 == 0:
            percent = round((sequence[i-1][1] // 10 * 10) * 0.02, 2)
            result = round(sequence[i-1][1] + percent + 0.2, 2)
        else:
            percent = round((sequence[i-1][1] // 10 * 10) * 0.02, 2)
            result = round(sequence[i-1][1] + percent + 0.4, 2)
        sequence.append((today + datetime.timedelta(days=i), result))

    return render_template("sequence.html", sequence=sequence)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
