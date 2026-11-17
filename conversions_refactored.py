#Mohammed Wasid IS211

class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, val):
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    temps = ["celsius", "fahrenheit", "kelvin"]
    distances = ["miles", "yards", "meters"]

    if fromUnit  in temps and toUnit not in temps:
        raise ConversionNotPossible
    if fromUnit  in distances and toUnit not in distances:
        raise ConversionNotPossible
    if fromUnit not in temps and fromUnit not in distances:
        raise ConversionNotPossible

    if fromUnit == "celsius":
        x = val
    elif fromUnit == "fahrenheit":
        x = (val - 32) * 5 / 9
    elif fromUnit == "kelvin":
        x = val - 273.15
    elif fromUnit == "meters":
        x = val
    elif fromUnit == "miles":
        x = val * 1609.344
    else:
        x = val * 0.9144

    if toUnit == "celsius":
        result = x
    elif toUnit == "fahrenheit":
        result = x * 9 / 5 + 32
    elif toUnit == "kelvin":
        result = x + 273.15
    elif toUnit == "meters":
        result = x
    elif toUnit == "miles":
        result = x / 1609.344
    else:
        result = x / 0.9144

    return float(result)



