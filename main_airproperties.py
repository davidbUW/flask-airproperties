"""
Functions to calculate air properties based on pressure, temperature and 
absolute humidity
-Temperatures must be -40F to 560F

Use saturation pressure data from air_properties_data.py

"""

def calculate_air_density(air_temperature, air_pressure):
    """
    Function to calculate air density based on pressure and temperature.
    Input - Pressure units - PSIA
    Input - Temeprature Units - F
    Output - Density Units - lb/ft^3
    """
    # try:
    air_density = (float(air_pressure)*144)/\
                (53.34*(float(air_temperature)+459.67))
    
    if air_pressure > 7000 or air_pressure < 0:
        raise ValueError
    elif air_temperature > 560 or air_temperature <-40:
        raise ValueError

    return air_density

def convert_humidity_absolute(humidity_absolute):
    """
    Function to convert absolute humdity units
    Input Units - gr/lb
    Output Units - kg/kg or lb/lb
    """
    humidity_absolute_kg_kg = float(humidity_absolute)/7000

    if humidity_absolute > 200 or humidity_absolute < 0:
            raise ValueError
            
    return humidity_absolute_kg_kg


def get_saturation_pressure(saturation_pressure_data, air_temperature):
    """
    Function to lookup saturation pressure based on air temperature.
    Input - Temeprature Units - F
    Output - Pressure Units - PSIA
    """
    # try:
    for temperature_upper in saturation_pressure_data:
        if temperature_upper[0] >= float(air_temperature):
            break

    for temperature_lower in reversed(saturation_pressure_data):
        if temperature_lower[0] <= float(air_temperature):
            break

    if temperature_upper[0] == float(air_temperature):
        saturation_pressure = temperature_lower[1]
    else:
        saturation_pressure = (((float(air_temperature)-temperature_upper[0])*
                                (temperature_lower[1]-temperature_upper[1]))/
                                (temperature_lower[0]-temperature_upper[0]))+\
                                    temperature_upper[1]
    # except:
    if air_temperature > 560 or air_temperature <-40:
        raise ZeroDivisionError
    return saturation_pressure

def calculate_relative_humidity(humidity_absolute_kg_kg, air_pressure, \
                                saturation_pressure):
    """
    Function to calculate relativity humidity based on absolute humidity,
    saturation pressure and temperature.
    Input - Absolute Humidity Units - kg/kg or lb/lb
    Input - Pressure units - PSIA
    Input - Temeprature Units - F
    Output - Relative Humidty - %
    """
    # try:
    humidity_relative = (float(humidity_absolute_kg_kg)*float(air_pressure))/\
                ((0.622 + float(humidity_absolute_kg_kg))* \
                    float(saturation_pressure))

    if humidity_relative > 1:
        humidity_relative = None
    # except:
    if air_pressure > 7000 or air_pressure < 0:
        raise ValueError

    return humidity_relative

def calculate_vapor_pressure(saturation_pressure, humidity_relative):
    """
    Function to calculate vapor pressure based on saturation pressure and
    relative humidity.
    Input - Relative Humidty - %
    Input - Pressure units - PSIA
    Output - Pressure units - PSIA
    """
    vapor_pressure = float(saturation_pressure) * float(humidity_relative)
    return vapor_pressure
