from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    name = ""
    upper_name = ""
    length = 0

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        upper_name = name.upper()
        length = len(name)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template(
        "index.html",
        original_name=name,
        upper_name=upper_name,
        length=length,
        time=current_time
    )

if __name__ == "__main__":
    app.run(debug=True)
