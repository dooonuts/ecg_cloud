import sys
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

@app.route('/instant')
def instant():
  return 'instant'

@app.route('/average')
def average():
  return 'average'

@app.route('/anomaly')
def anomaly():
  return 'anomaly'
 
if __name__ == '__main__':
  app.run(debug=True, host= '0.0.0.0', port=5000)
