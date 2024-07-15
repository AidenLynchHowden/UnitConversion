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
        self.assertAlmostEqual(value_out, 689475.7293, places=3)
        
    def test_6(self):
        value_out = convert(value_in=123.33, units_from='psi', units_to='pa')
        self.assertAlmostEqual(value_out, 850330.417, places=3)
        
    def test_7(self):
        value_out = convert(value_in=235654, units_from='kpa', units_to='pa')
        self.assertAlmostEqual(value_out, 235654000, places=3)
        
    def test_8(self):
        value_out = convert(value_in=854642, units_from='mpa', units_to='pa')
        self.assertAlmostEqual(value_out, 854642000000, places=3)
        
    def test_9(self):
        value_out = convert(value_in=654346, units_from='kgcm2', units_to='pa')
        self.assertAlmostEqual(value_out, 64169422009, places=3)
        
    def test_10(self):
        value_out = convert(value_in=100, units_from='C', units_to='F')
        self.assertAlmostEqual(value_out, 212, )