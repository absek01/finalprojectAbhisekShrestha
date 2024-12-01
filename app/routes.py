from flask import Blueprint, render_template, request, flash

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("home.html")

@main.route("/scan", methods=["POST"])
def scan():
    target_url = request.form.get("target_url")
    if not target_url:
        flash("Please enter a valid URL", "error")
        return render_template("home.html")
    # Logic to interact with ZAP API will go here
    return f"Scanning {target_url}..."