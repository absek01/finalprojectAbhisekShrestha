from flask import Blueprint, render_template, request, flash
from .zap_client import ZAPClient
from config import Config

main = Blueprint("main", __name__)

zap_client = ZAPClient(api_key=Config.ZAP_API_KEY, base_url=Config.ZAP_BASE_URL)


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/scan", methods=["POST"])
def scan():
    target_url = request.form.get("target_url")
    if not target_url:
        flash("Please enter a valid URL", "error")
        return render_template("home.html")

    try:
        zap_client.start_scan(target_url)
        alerts = zap_client.get_alerts(target_url)
        return render_template("scan_results.html", alerts=alerts)
    except Exception as e:
        flash(f"Error: {str(e)}", "error")
        return render_template("home.html")
