import unittest
from eyes_on_me import lights
import eyes_on_me.config


class LightsTemperatureTest(unittest.TestCase):
    def get_temperature_for_light_regular_test(self):
        eyes_on_me.config.mock_config(
            {
                "wb-balance": {
                    "min": 3500,
                    "normal": 4000,
                    "max": 6000
                }
            })

        self.assertAlmostEqual(
            lights.get_temperature_for_light(0.0),
            3500
        )

        self.assertAlmostEqual(
            lights.get_temperature_for_light(1.0),
            6000
        )

        self.assertAlmostEqual(
            lights.get_temperature_for_light(0.6),
            4400
        )

        self.assertAlmostEqual(
            lights.get_temperature_for_light(0.3),
            3800
        )

    def equal_wb_for_min_and_normal_test(self):
        eyes_on_me.config.mock_config(
            {
                "wb-balance": {
                    "min": 3500,
                    "normal": 3500,
                    "max": 3500
                }
            })
        self.assertAlmostEqual(
            lights.get_temperature_for_light(0.0),
            3500
        )

        self.assertAlmostEqual(
            lights.get_temperature_for_light(1.0),
            3500
        )

        self.assertAlmostEqual(
            lights.get_temperature_for_light(0.6),
            3500
        )


class LightsBacklightTest(unittest.TestCase):
    def get_backlight_for_light_regular_test(self):
        eyes_on_me.config.mock_config(
            {
                "backlight": {
                    "min": 5,
                    "normal": 30,
                    "max": 45
                }
            })

        self.assertAlmostEqual(
            lights.get_backlight_for_light(0.0),
            5.0)

        self.assertAlmostEqual(
            lights.get_backlight_for_light(0.5),
            30)

        self.assertAlmostEqual(
            lights.get_backlight_for_light(1.0),
            45)

        self.assertAlmostEqual(
            lights.get_backlight_for_light(0.6),
            33.0)

        self.assertAlmostEqual(
            lights.get_backlight_for_light(0.3),
            20.0)

    def equal_backlight_for_min_and_normal_test(self):
        eyes_on_me.config.mock_config(
            {
                "backlight": {
                    "min": 5,
                    "normal": 5,
                    "max": 5
                }
            })

        self.assertAlmostEqual(
            lights.get_backlight_for_light(0.0),
            5.0)

        self.assertAlmostEqual(
            lights.get_backlight_for_light(0.5),
            5.0)

        self.assertAlmostEqual(
            lights.get_backlight_for_light(1.0),
            5.0)

        self.assertAlmostEqual(
            lights.get_backlight_for_light(0.6),
            5.0)

        self.assertAlmostEqual(
            lights.get_backlight_for_light(0.3),
            5.0)


class StrategyChooserTests(unittest.TestCase):
    def timed_strategy_chooser_test(self):
        eyes_on_me.config.mock_config(
            {"strategy": "timed",
             "timed-strategy": {
                 "light-table": {
                     "dawn": 0.2,
                     "sunrise": 0.6,
                     "noon": 1.0,
                     "sunset": 0.6,
                     "dusk": 0.2
                 }}})
        self.assertEqual(lights.choose_strategy().__class__.__name__,
                         "TimedStrategy")

    def webcam_strategy_chooser_test(self):
        eyes_on_me.config.mock_config({"strategy": "webcam"})
        self.assertEqual(lights.choose_strategy().__class__.__name__,
                         "WebcamStrategy")
