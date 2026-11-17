from conversions_refactored import ConversionNotPossible
import unittest
import conversions as cv
import conversions_refactored as cr

class TestConversions(unittest.TestCase):

    def test_c_to_k(self):
        cases = [(-25, 248.15), (-5, 268.15), (0, 273.15), (20, 293.15), (30, 303.15)]
        for c, target in cases:
            res = cv.convertCelsiusToKelvin(c)
            print("Converting", c, "Celsius to Kelvin should give", target, "and we got ", res)
            self.assertAlmostEqual(res, target, places=2)

    def test_c_to_f(self):
        cases = [(-25, -13), (-5, 23), (0, 32), (20, 68), (30, 86)]
        for c, target in cases:
            res = cv.convertCelsiusToFahrenheit(c)
            print("Converting", c, "Celsius to Fahrenheit should give", target, "and we got ", res)
            self.assertAlmostEqual(res, target, places=2)

    def test_f_to_c(self):
        cases = [(-13, -25), (23, -5), (32, 0), (68, 20), (86, 30)]
        for f, target in cases:
            res = cv.convertFahrenheitToCelsius(f)
            print("Converting", f, "Fahrenheit to Celsius should give", target, "and we got ", res)
            self.assertAlmostEqual(res, target, places=2)

    def test_f_to_k(self):
        cases = [(-13, 248.15), (23, 268.15), (32, 273.15), (68, 293.15), (86, 303.15)]
        for f, target in cases:
            res = cv.convertFarhenheitToKelvin(f)
            print("Converting", f, "Fahrneheit to Kelvin should give", target, "and we got ", res)
            self.assertAlmostEqual(res, target, places=2)

    def test_k_to_c(self):
        cases = [(248.15, -25), (268.15, -5), (273.15, 0), (293.15, 20), (303.15, 30)]
        for k, target in cases:
            res = cv.convertKelvinsToCelsius(k)
            print("Converting", k, "Kelvin to Celsius should give", target, "and we got ", res)
            self.assertAlmostEqual(res, target, places=2)

    def test_k_to_f(self):
        cases = [(248.15, -13), (268.15, 23), (273.15, 32), (293.15, 68), (303.15, 86)]
        for k, target in cases:
            res = cv.convertKelvinsToFahrenheit(k)
            print("Converting", k, "Kelvin to Fahrenheit should give", target, "and we got ", res)
            self.assertAlmostEqual(res, target, places=2)

    def test_temps(self):
        cases = [("Fahrenheit", "Celsius", -13, -25),
                 ("Fahrenheit", "Kelvin", -13, 248.15),
                 ("Celsius", "Fahrenheit", -25, -13),
                 ("Celsius", "Kelvin", -25, 248.15),
                 ("Kelvin", "Fahrenheit", 248.15, -13),
                 ("Kelvin", "Celsius", 248.15, -25)]
        for frm, to, val, target in cases:
            res =  cr.convert(frm, to, val)
            print("Converting", val, frm, "to", to, "should give", target, "and we got ", res)
            self.assertAlmostEqual(res, target, places=2)

    def test_dists(self):
        cases = [("Yards", "Meters", 100, 91.44),
                 ("Meters", "Yards", 91.44, 100),
                 ("Yards", "Miles", 1760, 1),
                 ("Miles", "Yards", 1, 1760),
                 ("Miles", "Meters", 1, 1609.344),
                 ("Meters", "Miles", 1609.344, 1)]
        for frm, to, val, target in cases:
            res = cr.convert(frm, to, val)
            print("Converting", val, frm, "to", to, "should give", target, "and we got ", res)
            self.assertAlmostEqual(res, target, places=2)

    def test_same_units(self):
        cases = ["Celsius", "Fahrenheit", "Kelvin", "Miles", "Yards", "Meters"]
        for c in cases:
            res = cr.convert(c, c, 100)
            print("Converting 100", c, "to", c, "should give 100 and we got ", res)
            self.assertAlmostEqual(res, 100, places=2)

    def test_bad_units(self):
        cases = [("Yards", "Fahrenheit"), ("Miles", "Celsius"), ("Meters", "Kelvin"),
                 ("Fahrenheit", "Yards"), ("Celsius", "Miles")]
        for frm, to in cases:
            print("Converting", frm, "to", to, "should raise the exception")
            self.assertRaises(ConversionNotPossible, cr.convert, frm, to, 100)

if __name__ == "__main__":
    unittest.main()