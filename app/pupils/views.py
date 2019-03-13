from app import *
from app.Database.models import *

pupil=Blueprint('pupil', __name__)

class Create_Pupil(MethodView):
    def post(self):
        request_data=request.get_json()
        if type(request_data['name'])==int:
            response={
                "Message":"Name Cannot be Numeric"
            }
            return make_response(jsonify(response)), 401
        
        elif type(request_data['guardian'])==int:
            response={
                "Message":"Parent Name Cannot be Numeric"
            }
            return make_response(jsonify(response)), 401
        
        elif type(request_data['class_stream'])==int:
            response={
                "Message":"Class Stream Cannot be Numeric"
            }
            return make_response(jsonify(response)), 401

        else:
            Pupil.addPupil(request_data['name'], request_data['date_of_birth'], request_data['age'], request_data['class_stream'], request_data['guardian'], request_data['phone_number'], request_data['school_id'])
            response={
                "Message":"Successfully Registerd Pupil"
            }
            return make_response(jsonify(response)), 201

class Search_Pupil(MethodView):
    def get(self, school_id):
        get_pupil=Pupil.query.filter_by(school_id=school_id).first()
        toStr=str(get_pupil)
        toLoading=json.loads(toStr)
        return make_response(jsonify(toLoading)), 200

create_pupil=Create_Pupil.as_view('create_pupil')
search_pupil=Search_Pupil.as_view('search_pupil')

pupil.add_url_rule('/pupil/<string:school_id>', view_func=search_pupil, methods=['GET'])
pupil.add_url_rule('/auth/pupil/Register', view_func=create_pupil, methods=['POST'])