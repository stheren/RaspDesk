from flask import Flask, redirect, url_for
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix='/')


@app.errorhandler(404)
def not_found(e):
  return "<h1 style=\"text-align: center; font-size: 100px;\">404 : Not Found</h1>"

if(__name__) == '__main__':
    app.run(debug=True, port=8080)