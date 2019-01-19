# import Flask class
from flask import Flask, render_template, request
import os, sys

# create application object
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# use decorator pattern
# to link the view function to a url
@app.route("/")
@app.route("/hello")
# view function
def hello_world():
    return "Hello, World!"

@app.route("/test", methods=['GET', 'POST'])
# view function
def test_function():
    global count
    count += 1
    if(count != 1):
        if(request.method == 'GET'):
            return render_template('index.html', count_=count)
        if(request.method == 'POST'):
            sample_count = count * 10
            command = "python3 test_image.py " + str(sample_count) + " " + str(request.form['pic'])
            print('command: ', command)
            os.system(command)
            return render_template('index.html', count_=count, image=request.form['pic'])
    if(request.method == 'POST'):
        print(request.form['pic'])
    return ("First time, haan? You entered: ")

@app.route("/test", methods=['POST'])
def form_post():
    text = request.form['pic']
    return text

# https://stackoverflow.com/questions/45583828/python-flask-not-updating-images
# No caching at all for API endpoints.
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
    return response

if __name__ == "__main__":
    count = 0
    app.run()