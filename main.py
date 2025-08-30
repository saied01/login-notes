from website import create_app
from website import Config


app = create_app()



if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])