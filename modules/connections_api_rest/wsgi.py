import os

from app.application import create_app

app = create_app(os.getenv("FLASK_ENV") or "test")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
