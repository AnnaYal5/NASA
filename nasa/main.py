from flask import Flask, render_template
from API import response

app = Flask(__name__)

def get_nasa_picture():
    if response.status_code == 200:
        data = response.json()
        hd_image_url = data.get("hdurl")
        title = data.get("title")
        explanation = data.get("explanation")

        return hd_image_url, title, explanation
    else:
        return None, None, "Помилка"


@app.route("/api")
def index():
    hd_image_url, title, explanation = get_nasa_picture()

    if hd_image_url:
        return render_template("index.html", hd_image_url=hd_image_url, title=title,  explanation=explanation)
    else:
        return "Зображення не знайдено."


if __name__ == '__main__':
    app.run(debug=True)
