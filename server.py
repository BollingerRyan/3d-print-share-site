from flask_app import app
from flask_app.controllers import navigation
from flask_app.controllers import user_controller
from flask_app.models import user_model
from flask_app.controllers import profile_controller
from flask_app.models import profile_model
if __name__=='__main__':
    app.run(debug=True)

app.secret_key = 'secret'