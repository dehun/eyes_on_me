import unittest

from eyes_on_me.webcam_strategy import WebcamStrategy
import eyes_on_me.config


class WebcamStrategyTests(unittest.TestCase):
    def test_lightning_of_black_image_000000(self):
        eyes_on_me.config.mock_config({"webcam-strategy": {"coeff": 0.6}})
        strategy = WebcamStrategy()
        self.assertAlmostEqual(
            strategy._get_image_lightning("./data/black_000000.jpg"),
            0.0, 2)

    def test_lightning_of_blue_image_0000bb(self):
        eyes_on_me.config.mock_config({"webcam-strategy": {"coeff": 0.6}})
        strategy = WebcamStrategy()
        self.assertAlmostEqual(
            strategy._get_image_lightning("./data/black_0000bb.jpg"),
            187.0 / 255 * 0.6, 2)

    def test_lightning_of_real_photo(self):
        eyes_on_me.config.mock_config({"webcam-strategy": {"coeff": 0.6}})
        strategy = WebcamStrategy()
        self.assertAlmostEqual(
            strategy._get_image_lightning("./data/real_photo.jpg"),
            0.588, 2)

    def test_lightning_of_white_image_ffffff(self):
        eyes_on_me.config.mock_config({"webcam-strategy": {"coeff": 0.6}})
        strategy = WebcamStrategy()
        self.assertAlmostEqual(
            strategy._get_image_lightning("./data/white_ffffff.jpg"),
            0.6, 2)
