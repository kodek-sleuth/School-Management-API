from app import *
from app.Database.models import *

results_bot=Blueprint('results_bot', __name__)

class Bot_Results(MethodView):
    def get(self, pupil_id):    
        pupil=Pupil.query.filter_by(id=pupil_id).first()
        toStr= str(pupil.english_bot)
        loadingJson=json.loads(toStr)
        return make_response(jsonify(loadingJson)),200

bot_results=Bot_Results.as_view('bot_results')
results_bot.add_url_rule('/pupil/bot/results/<int:pupil_id>', view_func=bot_results, methods=['GET'])