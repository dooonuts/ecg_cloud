import sys
import json
import controller
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/data', methods=['POST'])
def postJSONHandler():
    print("Here")
    if(request.is_json):
        content = request.get_json()
        print(content)
    return 'content'


@app.route('/api/requests', methods=['GET'])
def counter():
  #  count = count+1;
   return count


@app.route('/api/heart_rate/summary', methods=['POST'])
def instantaneous():
  #  count = count+1;
    if(request.is_json):
        data_dict = request.get_json()
        print(data_dict)
        [time, instant_hr, tachy, brady] =  controller.summary(data_dict)
        # [tachy, brady] = controller.summary(data_dict)
        # jsonify the lists
        return_dict = {
            "time": time,
            "instantaneous_heart_rate": instant_hr,
            "tachycardia_annotations": tachy,
            "bradycardia_annotations": brady}
        # return_dict = {
        #    "tachycardia_annotations": tachy,
        #    "bradycardia_annotations": brady}
        json_info = json.dumps(return_dict)
        return json_info
    else:
        raise ValueError("Did not input a JSON file")


@app.route('/api/heart_rate/average', methods=['POST'])
def average():
   # count=count+1
    if(request.is_json):
        data_dict = request.get_json()
        [avg_per, time_int, average_hr, tachy,
            brady] = controller.average(data_dict)
        # jsonify the lists
        return_dict = {
            "averaging_period": avg_per,
            "time_interval": time_int,
            "average_heart_rate": average_hr,
            "tachycardia_annotations": tachy,
            "bradycardia_annotations": brady}
        json_info = json.dumps(return_dict)
        return json_info
    else:
        raise ValueError("Did not input a JSON file")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
