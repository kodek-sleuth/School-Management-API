from app import *

admin=Blueprint('admin', __name__)

class LoginView(MethodView):
    def get(self):
        return 'Hello World'

loginview=LoginView.as_view('loginview')
admin.add_url_rule('/auth/admin/Login', view_func=loginview, methods=['GET'])