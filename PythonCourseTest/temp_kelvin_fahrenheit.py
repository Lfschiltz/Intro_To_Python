def to_kelvin(fahrenheit):
  kelvin = (fahrenheit + 459.67) * 5/9
  return kelvin

def to_fahrenheit(kelvin):
  fahrenheit = kelvin * 9/5 - 459.67
  return fahrenheit
