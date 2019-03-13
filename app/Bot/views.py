from app import *
from app.Database.models import *

subject_bot=Blueprint('subject_bot', __name__)

class Math_Bot_Register(MethodView):
    def post(self, pupil_id):
        request_data=request.get_json()
        if type(request_data['teacher'])==int:
            response={
                "Message":"Teacher's Name Cannot be Numeric"
            }
            return make_response(jsonify(response)), 401
        
        else:
            Math_Bot.mark_subject(request_data['marks'], request_data['aggregate'], request_data['teacher'], pupil_id)
            response={
                "Message":"Successfully Registerd Marks"
            }
            return make_response(jsonify(response)), 201

class English_Bot_Register(MethodView):
    def post(self, pupil_id):
        request_data=request.get_json()
        if type(request_data['teacher'])==int:
            response={
                "Message":"Teacher's Name Cannot be Numeric"
            }
            return make_response(jsonify(response)), 401
        
        else:
            English_Bot.mark_subject(request_data['marks'], request_data['aggregate'], request_data['teacher'], pupil_id)
            response={
                "Message":"Successfully Registerd Marks"
            }
            return make_response(jsonify(response)), 201

class Science_Bot_Register(MethodView):
    def post(self, pupil_id):
        request_data=request.get_json()
        if type(request_data['teacher'])==int:
            response={
                "Message":"Teacher's Name Cannot be Numeric"
            }
            return make_response(jsonify(response)), 401
        
        else:
            Science_Bot.mark_subject(request_data['marks'], request_data['aggregate'], request_data['teacher'], pupil_id)
            response={
                "Message":"Successfully Registerd Marks"
            }
            return make_response(jsonify(response)), 201

class Sst_Bot_Register(MethodView):
    def post(self, pupil_id):
        request_data=request.get_json()
        if type(request_data['teacher'])==int:
            response={
                "Message":"Teacher's Name Cannot be Numeric"
            }
            return make_response(jsonify(response)), 401
        
        else:
            Sst_Bot.mark_subject(request_data['marks'], request_data['aggregate'], request_data['teacher'], pupil_id)
            response={
                "Message":"Successfully Registerd Marks"
            }
            return make_response(jsonify(response)), 201

class Quran_Bot_Register(MethodView):
    def post(self, pupil_id):
        request_data=request.get_json()
        if type(request_data['teacher'])==int:
            response={
                "Message":"Teacher's Name Cannot be Numeric"
            }
            return make_response(jsonify(response)), 401
        
        else:
            Quran_Bot.mark_subject(request_data['marks'], request_data['aggregate'], request_data['teacher'], pupil_id)
            response={
                "Message":"Successfully Registerd Marks"
            }
            return make_response(jsonify(response)), 201

class Arabic_Bot_Register(MethodView):
    def post(self, pupil_id):
        request_data=request.get_json()
        if type(request_data['teacher'])==int:
            response={
                "Message":"Teacher's Name Cannot be Numeric"
            }
            return make_response(jsonify(response)), 401
        
        else:
            Arabic_Bot.mark_subject(request_data['marks'], request_data['aggregate'], request_data['teacher'], pupil_id)
            response={
                "Message":"Successfully Registerd Marks"
            }
            return make_response(jsonify(response)), 201

class Fiqhul_Bot_Register(MethodView):
    def post(self, pupil_id):
        request_data=request.get_json()
        if type(request_data['teacher'])==int:
            response={
                "Message":"Teacher's Name Cannot be Numeric"
            }
            return make_response(jsonify(response)), 401
        
        else:
            Fiqul_Libaadaat_Bot.mark_subject(request_data['marks'], request_data['aggregate'], request_data['teacher'], pupil_id)
            response={
                "Message":"Successfully Registerd Marks"
            }
            return make_response(jsonify(response)), 201


math_bot_register=Math_Bot_Register.as_view('math_bot_register')
english_bot_register=English_Bot_Register.as_view('english_bot_register')
science_bot_register=Science_Bot_Register.as_view('science_bot_register')
sst_bot_register=Sst_Bot_Register.as_view('sst_bot_register')
quran_bot_register=Quran_Bot_Register.as_view('quran_bot_register')
arabic_bot_register=Sst_Bot_Register.as_view('arabic_bot_register')
fiqhul_bot_register=Fiqhul_Bot_Register.as_view('fiqhul_bot_register')


subject_bot.add_url_rule('/pupil/bot/math/<int:pupil_id>', view_func=math_bot_register, methods=['POST'])
subject_bot.add_url_rule('/pupil/bot/english/<int:pupil_id>', view_func=english_bot_register, methods=['POST'])
subject_bot.add_url_rule('/pupil/bot/science/<int:pupil_id>', view_func=science_bot_register, methods=['POST'])
subject_bot.add_url_rule('/pupil/bot/sst/<int:pupil_id>', view_func=sst_bot_register, methods=['POST'])
subject_bot.add_url_rule('/pupil/bot/quran/<int:pupil_id>', view_func=quran_bot_register, methods=['POST'])
subject_bot.add_url_rule('/pupil/bot/arabic/<int:pupil_id>', view_func=arabic_bot_register, methods=['POST'])
subject_bot.add_url_rule('/pupil/bot/fiqhul/<int:pupil_id>', view_func=fiqhul_bot_register, methods=['POST'])