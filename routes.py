import sys
import json
from flask import Flask, request, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/data',methods = ['POST'])
def postJSONHandler():
  if(request.is_json):
    content=request.get_json()
    print('content',file=sys.stdout)
  return 'content'

@app.route('/api/heart_rate/summary', methods= ['POST'])
def instantaneous():
  if(request.is_json):
    data_dict = request.json();

    
 
if __name__ == '__main__':
  app.run(debug=True, host= '0.0.0.0', port=5000)
