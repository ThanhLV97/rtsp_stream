import os
import cv2
from util.base_camera import BaseCamera


class Camera(BaseCamera):

    def frames(self):
        camera = cv2.VideoCapture(self.video_source_set)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            ret, img = camera.read()
            if not ret:
                continue
            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
