
from views import app


if __name__ == "__main__":
    from config import DEBUG
    if DEBUG:
        app.run("0.0.0.0", debug=True)
    else:
        app.run("0.0.0.0")
