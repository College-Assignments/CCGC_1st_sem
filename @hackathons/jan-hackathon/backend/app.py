import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import helper
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
# to simplify the data access, we just use a .json for the template
FILE_PATH = "data/"
USER_DATA_PATH = FILE_PATH+"userdata.json"
FOOD_DATA_PATH = FILE_PATH+"food.json"
try:
    user_email = os.getenv("SENDER_EMAIL")
except:
    print("""please define SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL and OPENAI_API_KEY in ENV VAR e.g
                please config your env:
                SENDER_EMAIL=humbertechsociety@gmail.com
                RECEIVER_EMAIL=humbertechsociety@gmail.com
                SENDER_PASSWORD=xxx
                OPENAI_API_KEY=xxx
            """ )

CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
  
@app.route("/data", methods=["GET"])
def get_data():
    with open(USER_DATA_PATH) as f:
        data = json.load(f)
    return jsonify(data)
  
@app.route("/add_data", methods=["POST"])
def add_data():
    food_name = request.json.get('food_name')
    food_data={}
    user_data={}
    with open(USER_DATA_PATH, "r") as f:
        print(user_email)
        user_data = json.load(f)
        if "food_consumed" not in user_data[user_email]:
            user_data[user_email]["food_consumed"] = {}

        with open(FOOD_DATA_PATH, "r") as f:
            food_data = json.load(f)
            if food_name in food_data:
                current_time = datetime.now().strftime("%m/%d/%y %H:%M")
                if current_time not in user_data[user_email]["food_consumed"]:
                    user_data[user_email]["food_consumed"][current_time] = []
                # restructure
                new_food_data = {}
                new_food_data = food_data[food_name]
                new_food_data['name'] = food_name
                user_data[user_email]["food_consumed"][current_time].append(new_food_data)

                print('{} has been added'.format(food_name))
            else:
                return "no food info for {}".format(food_name)  

    with open(USER_DATA_PATH, "w") as f:
        json.dump(user_data, f)

    alert_bool = helper.history_tracker(USER_DATA_PATH, user_email)
    if alert_bool:
        helper.send_email('Health Risk Alert!!')
    return "Done adding, {}!".format(food_name)
    # return jsonify({"message": "Data added successfully."})


@app.route("/food", methods=["GET"])
def get_foods():
    with open(FOOD_DATA_PATH) as f:
        foods = json.load(f)

    return jsonify(foods)

def init_userdata():
    # to skip the authentication, we just hardcode here for now
    user_data = ""

    with open(USER_DATA_PATH, "r") as f:
        user_data = json.load(f)
        # feel free to modify it
        if user_email not in user_data:
            user_data[user_email] = {
                    "id": 13,
                    "first_name": "Humber",
                    "last_name": "ABC",
                    "age": 27,
                    "height_cm": 170,
                    "weight_kg": 70
            }
        print(user_data)
    
    with open(USER_DATA_PATH, "w+") as f:
        json.dump(user_data, f)

if __name__ == "__main__":
    init_userdata()
    #helper.gen_openai_image()
    # testing
    app.run(host='0.0.0.0', port=5001, debug=True)

