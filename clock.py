from flask import Flask, render_template
import time
from threading import Thread

clock = Flask(__name__)

current_time = ""

def update_time():
    global current_time
    while True:
        current_time = time.strftime('%H:%M:%S')
        time.sleep(1)

@clock.route('/')
def index():
    return render_template('index.html', current_time=current_time)

@clock.route('/time')
def get_time():
    return current_time

if __name__ == '__main__':
    time_thread = Thread(target=update_time)
    time_thread.daemon = True
    time_thread.start()
    clock.run(debug=True, host='0.0.0.0')