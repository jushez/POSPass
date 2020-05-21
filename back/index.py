from flask import Blueprint, render_template

indexgg = Blueprint("gabor", __name__)


@indexgg.route("/")
def index():
    return "Index.. hahaha"