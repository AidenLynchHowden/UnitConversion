def convert(value_in: float, units_from: str, units_to: str) -> float:
    units_to_si = {
        'pa':       ('pressure', 1, 0),
        'bar':      ('pressure', 1e5, 0),
        'psi':      ('pressure', 6894.7572931783, 0), 
        'kpa':      ('pressure', 1000, 0),
        'mpa':      ('pressure', 1000000, 0),
        'kgcm2':    ('pressure', 98066.5, 0),
        'K':        ('temperature', 1, 0),
        'F':        ('temperature', 5/9, 229835/900),
        'C':        ('temperature', 1, 273.15),
    }
    
    if units_from not in units_to_si or units_to not in units_to_si:
        raise ValueError("Unsupported unit")
    
    (category_from, a_from, b_from) = units_to_si[units_from]  # Go over this one more time?
    (category_to, a_to, b_to) = units_to_si[units_to]
    
    if category_from != category_to:
        raise ValueError("Cannot convert different categories")
    
    value_in_si = value_in * a_from + b_from # turns input into K = si equivelant
    value_out = (value_in_si - b_to) / a_to # Converts si to the user input
    return value_out



