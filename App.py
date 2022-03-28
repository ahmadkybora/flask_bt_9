from config import app
from flask_migrate import Migrate
from routes import userRoute
from app.Controllers.UserController import UserController

#@app.route("/")
# us = UserController()
# us.index()

app.register_blueprint(userRoute, url_prefix="/")
if __name__ == '__main__':
    app.run(debug=True)

