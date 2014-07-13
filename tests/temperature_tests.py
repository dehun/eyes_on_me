import unittest

from eyes_on_me import temperature


class RgbConversationTests(unittest.TestCase):
    def color_temperature_to_rgb_underflow_value_test(self):
        min_kelvin = min(temperature.kelvin_table.keys())
        self.assertEqual(
            temperature.color_temperature_to_rgb(min_kelvin / 2),
            temperature.kelvin_table[min_kelvin])
        self.assertEqual(
            temperature.color_temperature_to_rgb((min_kelvin - 15) / 3),
            temperature.kelvin_table[min_kelvin])
        self.assertEqual(
            temperature.color_temperature_to_rgb(min_kelvin - 5000),
            temperature.kelvin_table[min_kelvin])

    def color_temperature_to_rgb_overflow_value_test(self):
        max_kelvin = max(temperature.kelvin_table.keys())
        self.assertEqual(
            temperature.color_temperature_to_rgb(max_kelvin * 2),
            temperature.kelvin_table[max_kelvin])
        self.assertEqual(
            temperature.color_temperature_to_rgb((max_kelvin + 15) * 3),
            temperature.kelvin_table[max_kelvin])
        self.assertEqual(
            temperature.color_temperature_to_rgb(max_kelvin + 1500),
            temperature.kelvin_table[max_kelvin])

    def color_temperature_to_rgb_regular_conversation_tests(self):
        self.assertEqual(
            temperature.color_temperature_to_rgb(1200),
            temperature.kelvin_table[1000])
        self.assertEqual(
            temperature.color_temperature_to_rgb(1600),
            temperature.kelvin_table[1500])
        self.assertEqual(
            temperature.color_temperature_to_rgb(7633),
            temperature.kelvin_table[7500])

    def normalized_rgb_to_color_temperature_conversation_tests(self):
        self.assertEqual(
            temperature.normalized_rgb_to_color_temperature((2.33, 1.0, 0.0)),
            1500)
        self.assertEqual(
            temperature.normalized_rgb_to_color_temperature((1.86, 1.0, 0.13)),
            2000)
