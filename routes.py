import sys
import json
import controller
from flask import Flask, request, render_template

app = Flask(__name__)
count = 0


@app.route('/')
def home():
    """Template for home of webpage

       :rtype: home template on html
    """

    return render_template('home.html')


@app.route('/about')
def about():
    """Template for about for our webpage

       :rtype: about template on html
    """

    return render_template('about.html')


@app.route('/data', methods=['POST'])
def postJSONHandler():
    """Function to test handling data from JSON

       :rtype: the JSON content
    """

    if(request.is_json):
        content = request.get_json()
    return 'content'


@app.route('/api/requests', methods=['GET'])
def counter():
    #  count = count+1;
    global count
    count = count + 1
    print(count)
    json_count = json.dumps(count)
    return json_count


@app.route('/api/heart_rate/summary', methods=['POST'])
def instantaneous():
    """Function called when summary route is typed

        Takes in Post only

        :rtype: json to return to user or a Value Error
    """

    global count
    count = count + 1
    try:
        if(request.is_json):
            data_dict = request.get_json()
            print(data_dict)
            [time, instant_hr, tachy, brady] = controller.summary(data_dict)
            # [tachy, brady] = controller.summary(data_dict)
            # jsonify the lists
            return_dict = {
                    "time": time,
                    "instantaneous_heart_rate": instant_hr,
                    "tachycardia_annotations": tachy,
                    "bradycardia_annotations": brady}
            # return_dict = {
            #    "tachycardia_annotations": tachy,
            #    "bradycardia_annotations": brady
            json_info = json.dumps(return_dict)
            return json_info
        else:
            return 400
    except ValueError as err:
        sys.exit(-1)


@app.route('/api/heart_rate/average', methods=['POST'])
def average():
    """Function called when average route is typed

       Takes in Post only

       :rtype: json to return to user or a Value Error
    """

    global count
    count = count + 1
    try:
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
            return 400
    except ValueError as err:
        sys.exit(-1)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
