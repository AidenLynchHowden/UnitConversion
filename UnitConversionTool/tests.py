from UnitConversionTool.convert import convert
import unittest

class TestConvert(unittest.TestCase):
    
    def test_1(self):
        value_out = convert(value_in=100.00, units_from='pa', units_to='pa')
        self.assertAlmostEqual(value_out, 100.00)
 
    def test_2(self):
        value_out = convert(value_in=123.33, units_from='pa', units_to='pa')
        self.assertAlmostEqual(value_out, 123.33)
        
    def test_3(self):
        value_out = convert(value_in=100, units_from='bar', units_to='pa')
        self.assertAlmostEqual(value_out, 10000000)
        
    def test_4(self):
        value_out = convert(value_in=123.33, units_from='bar', units_to='pa')
        self.assertAlmostEqual(value_out, 12333000)
        
    def test_5(self):
        value_out = convert(value_in=100, units_from='psi', units_to='pa')
        self.assertAlmostEqual(value_out, 689475.7293)
        
    def test_6(self):
        value_out = convert(value_in=123.33, units_from='psi', units_to='pa')
        self.assertAlmostEqual(value_out, 850330.417)