import logging
from website import create_app
from website import Config



# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


app = create_app()


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])