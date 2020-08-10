#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response
from util.camera_index import Cam_index
# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from util.camera_opencv import Camera

app = Flask(__name__)


# @app.route('/')
# def index():
#     """Video streaming home page."""
#     return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/<string:tang>/<string:id>')
def video_feed(tang, id):
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera(Cam_index[tang][id])),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    # app.run( threaded=True, debug=False)
    app.run(host='192.168.4.24',port=5502, threaded=True, debug=False)
