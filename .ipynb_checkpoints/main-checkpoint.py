from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
# import functional
from warnings import filterwarnings
filterwarnings("ignore")
app = Flask(__name__)
CORS(app)
api = Api(app)

class Pipe(Resource):

    def get(self):
        print("hello")


    def post(self):
        print("Welcome to our API!")
        # jsdata = request.data
        # abc = beautifulSoup1.get_data(jsdata)
        # print(abc)
        # print(abc['inning'])
        # if abc["inning"]==1:
        #     prediction = functional.model1(abc)
        # else:
        #     prediction = functional.model2(abc)
        # print(prediction)
        # return {
        #         "Team1":abc['team1'],
        #         "Team2":abc['team2'],
        #         "team1_probability": prediction[0][0],
        #        "team2_probability":prediction[0][1]}
    
api.add_resource(Pipe,"/")

if __name__ == "__main__":
    app.run(debug=True)