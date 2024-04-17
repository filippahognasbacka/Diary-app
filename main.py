from website import app
from website.db import init_db


if __name__ == "__main__":
    init_db(app)
    app.run(debug=True)