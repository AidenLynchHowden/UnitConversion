def convert(value_in: float, units_from: str, units_to: str) -> float:
    units_to_si = {
        'pa': 1,
        'bar': 1e5,
        'psi': 6894.7572931783, 
    }
    
    if units_from not in units_to_si or units_to not in units_to_si:
        raise ValueError("Unsupported unit")
    
    value_in_si = value_in * units_to_si[units_from]
    value_out = value_in_si / units_to_si[units_to]
    return value_out

