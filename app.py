from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database.db import initialize_db
from flask_restful import Api 
from resources.routes import initialize_routes


app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# app.json_encoder = CustomJSONEncoder
# cors = CORS(app, supports_credentials=True)
DB_URI = "mongodb+srv://kalibrasi:b4t@cluster0-fn2qx.gcp.mongodb.net/kalibrasi_prod?retryWrites=true&w=majority"
app.config["MONGODB_HOST"] = DB_URI
# app.config["MONGODB_SETTINGS"] = {"DB": "b4t"}
app.config["SECRET_KEY"] = "b4t"

initialize_db(app)
initialize_routes(api)

@app.route('/')
def index():
    return "Selamat Datang di B4T Kalibrasi API management"


app.run(debug=True)