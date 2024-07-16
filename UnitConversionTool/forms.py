from django.forms import (
    Form,
    FloatField,
    ChoiceField,
)

PRESSURE_UNITS = [
    ('pa', 'pa'),
    ('bar', 'bar'),
    ('psi', 'psi'),
    ('kpa', 'kpa'),
    ('mpa', 'mpa'),
    ('kgcm2', 'kgcm2'),
]

TEMPERATURE_UNITS = [         # The Class at line 22 would need to be changed to account for the temperature 
    ('K', 'K'),
    ('F', 'F'),
    ('C', 'C'),
]


CATEGORY_CHOICES = [
    ('pressure', 'Pressure'),
    ('temperature', 'Temperature')
]


ALL_UNITS = PRESSURE_UNITS + TEMPERATURE_UNITS


class UnitConversionForm(Form):
    value_in = FloatField(required=False)              # Value in being the label shows the user where to enter their value for conversion. 
    units_from = ChoiceField(choices=ALL_UNITS)
    units_to = ChoiceField(choices=ALL_UNITS)
    category = ChoiceField(choices=CATEGORY_CHOICES)
    
    def update_unit_choices(self, category: str):      # Self is the form. 
        options = []                                   # The [] Is the key for the data dictionary.
        
        if category == 'temperature':                  # This means that whatever category is selected the page updates accordingly.
            options = TEMPERATURE_UNITS
        elif category == 'pressure':
            options = PRESSURE_UNITS
        
        self.fields['units_from'].choices = options
        self.fields['units_to'].choices = options

