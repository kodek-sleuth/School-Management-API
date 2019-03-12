from app import *
from app.Database.models import *

admin=Blueprint('admin', __name__)

class SignUpView(MethodView):
    def post(self):
        request_data=request.get_json()
        if type(request_data['name'])==int:
            response={
                "Message":"Name Cannot be Numeric"
            }
            return make_response(jsonify(response)), 401

        else:
            Admin.addAdmin(request_data['name'], request_data['username'], request_data['password'])
            response={
                "Message":"Successfully Created Admin"
            }
            return make_response(jsonify(response)), 201

class LoginView(MethodView):
    def get(self):
        return 'Hello World'

login_view=LoginView.as_view('login_view')
sign_up_view=SignUpView.as_view('sign_up_view')
admin.add_url_rule('/auth/admin/Login', view_func=login_view, methods=['GET'])
admin.add_url_rule('/auth/admin/SignUp', view_func=sign_up_view, methods=['POST'])