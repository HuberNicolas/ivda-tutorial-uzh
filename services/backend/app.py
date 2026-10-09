import os

from src import app

if __name__ == "__main__":
    # Port 5001 instead of Flask's default 5000, which macOS uses for AirPlay
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))
