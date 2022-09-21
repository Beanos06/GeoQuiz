from flask import Flask

from geoquiz.flags.flags import flags_bp

app = Flask(__name__)

app.register_blueprint(flags_bp, url_prefix='/flags')


if __name__ == '__main__':
    app.run(debug=True)