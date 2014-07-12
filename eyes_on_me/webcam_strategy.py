import subprocess

from eyes_on_me.config import config
from eyes_on_me.strategy import LightningStrategy
import PIL.Image


class WebcamStrategy(LightningStrategy):
    def __init__(self):
        pass

    def _take_a_shot(self):
        shot_path = config["webcam-strategy"]["shot-path"]
        webcam_command = config["webcam-strategy"]["command"]
        subprocess.check_call(webcam_command % {"shot_path": shot_path},
                              shell=True)
        return shot_path

    def _get_image_lightning(self, path):
        image = PIL.Image.open(path)
        average_lightning = 128.0
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                average_lightning += max(image.getpixel((x, y)))

        average_lightning /= image.size[0] * image.size[1]
        average_lightning /= 255
        return average_lightning * config["webcam-strategy"]["coeff"]

    def get_lightning(self):
        return self._get_image_lightning(self._take_a_shot())
