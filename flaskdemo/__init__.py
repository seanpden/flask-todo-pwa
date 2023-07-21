from flask import Flask

app = Flask(
    __name__,
    static_folder="views/static",
    template_folder="views/templates",
)

import flaskdemo.controllers.home_page  # noqa: F401
