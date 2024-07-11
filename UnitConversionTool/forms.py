from django.forms import (
    Form,
    FloatField,
    ChoiceField,
)

PRESSURE_UNITS = [
    ('pa', 'pa'),
    ('bar', 'bar'),
    ('psi', 'psi'),
]


class UnitConversionForm(Form):
    value_in = FloatField(label='Value_in')             #Value in being the label shows the user where to enter their value for conversion. 
    units_from = ChoiceField(choices=PRESSURE_UNITS)
    units_to = ChoiceField(choices=PRESSURE_UNITS)