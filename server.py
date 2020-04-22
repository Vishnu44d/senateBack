## General flask stuf import
import os
from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from wtforms.validators import ValidationError

# default db stuff imports
from senateBack.config import DbEngine_config
from senateBack import create_db_engine, create_db_sessionFactory
from senateBack.models import createTables, destroyTables

# cross policy
from flask_cors import CORS
from dotenv import load_dotenv

#flask login stuffs
from flask_login import LoginManager
from flask_login import login_required, logout_user, current_user, login_user

#admin stuffs
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import FileUploadField
from senateBack.views.help import BlobUploadField

#api imports
from senateBack.api import *

load_dotenv()

engine = create_db_engine(DbEngine_config)
SQLSession = create_db_sessionFactory(engine)


login_manager = LoginManager()


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

login_manager.init_app(app)

CORS(app, supports_credentials=True)
@app.route('/')
def get():
    return "<h1> Hello, Welcome to backend </h1>"


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    from senateBack.models.userModel import User
    session = SQLSession()
    if user_id is not None:
        return session.query(User).filter_by(id=user_id).first()
    return None

@app.route('/login')
def load_user_from_request():
    try:
        api_key = request.args.get('api_key', None, type=str)

    except:
        "Not a valid arg"
    if api_key:
        from senateBack.auth.auth import validate_admin
        isValid, usr_ = validate_admin({'token': api_key})
        if isValid:
            login_user(usr_)
            # print("Logged in")
            return "<h1> Welcome {} </h1>".format(usr_.username)
        else:
            return "not valid user"
            
    else:
        return "No api key"


@app.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return "Sussussfully logout"


################# ADMIN WORK HERE
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='senate', template_mode='bootstrap3')
sess = SQLSession()


from senateBack.models.userModel import User
from senateBack.models.newsModel import News
from senateBack.models.bodyModel import Body
from senateBack.models.documentModel import Document
from senateBack.models.sliderModel import Slider
from senateBack.models.societiesModel import Societies
from senateBack.views import *

# admin.add_view(ProtectedView(User, sess))
admin.add_view(NewsView(News, sess))
admin.add_view(BodyView(Body, sess))
admin.add_view(DocView(Document, sess))
admin.add_view(SliderView(Slider, sess))
admin.add_view(SocView(Societies, sess))



app.register_blueprint(userBP, url_prefix='/user')
app.register_blueprint(contentBP, url_prefix='/content')



if __name__ == "__main__":
    app.run(debug=True)