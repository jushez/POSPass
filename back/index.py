from flask import Blueprint, render_template
# from flask_restful import Resource, Api
from main import api

indexgg = Blueprint("gabor", __name__, static_folder=".front/static", template_folder="./front/templates")


# @indexgg.route("/")
# def index():
#     return "Index.. hahaha"
api.add_resource(HelloWorld, '/')
