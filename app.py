from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_bmr(gender, weight, height, age):
    if gender == "female":
        return 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
    elif gender == "male":
        return 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    else:
        return None


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    # значения по умолчанию (пустая форма)
    form_data = {
        "gender": "female",
        "weight": "",
        "height": "",
        "age": "",
        "activity": "1.2"
    }

    if request.method == "POST":

        # если нажали "Рассчитать заново"
        if request.form.get("reset") == "1":
            return render_template(
                "index.html",
                result=None,
                form_data=form_data
            )

        # обычный расчёт
        form_data["gender"] = request.form["gender"]
        form_data["weight"] = request.form["weight"]
        form_data["height"] = request.form["height"]
        form_data["age"] = request.form["age"]
        form_data["activity"] = request.form["activity"]

        bmr = calculate_bmr(
            form_data["gender"],
            float(form_data["weight"]),
            float(form_data["height"]),
            int(form_data["age"])
        )

        result = round(bmr * float(form_data["activity"]), 2)

    return render_template(
        "index.html",
        result=result,
        form_data=form_data
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
