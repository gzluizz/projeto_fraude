from flask import Flask
from scripts.routes import main_bp

app = Flask(__name__)

# Registrar o Blueprint
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)
