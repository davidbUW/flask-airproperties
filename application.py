"""
Flask app to support air properties calculations

-address in browser http://localhost:5001/airproperties/
-terminate test server using control + c
"""

import re
from flask import Flask, render_template, request, redirect, url_for, session
import os
import main_airproperties, air_properties_data


application = Flask(__name__)

application.config['SECRET_KEY'] = 'random_secret_key'

@application.route('/')
def main():
    """
    Function to use route decorator for main page URL
    """
    return render_template('calculator.html')

@application.route('/about/')
def about():
    """
    Function to use route decorator for about page URL
    """
    return render_template('about.html')

@application.route('/calculate/', methods=["GET", "POST"])
def calculate():
    """
    Function to use route decorator for calculate page URL
    Function to input Temperature, Pressure and Absolute Humidity on web page 
    and output density, saturation pressure, relative humidity and aboslute 
    humidity in different units
    """
    if request.method == "POST":
        try:
            acceptable_temperature_range = "Temeprature must be -40F to 560F"
            acceptable_pressure_range = "Pressure must be 0psia to 7000psia"
            acceptable_humidity_range = "Humidity must be 0-200 gr/lb"
            high_humidity = "Humidity exceeds maximum allowed by pressure and \
            temperature combination"
            air_temperature = float(request.form["air_temperature"])
            air_pressure = float(request.form["air_pressure"])
            humidity_absolute = float(request.form["humidity_absolute"])

            density = main_airproperties.calculate_air_density(air_temperature, 
                                                            air_pressure)
            saturation_pressure = main_airproperties.\
                get_saturation_pressure(air_properties_data.\
                    saturation_pressure_data,air_temperature) 
            humidity_absolute_converted = main_airproperties.\
                convert_humidity_absolute(humidity_absolute)
            relative_humidity = 100 * main_airproperties.\
                calculate_relative_humidity(humidity_absolute_converted, \
                    air_pressure, saturation_pressure)
        
        except ZeroDivisionError:
            return render_template("calculator.html", \
                acceptable_temperature_range=acceptable_temperature_range,
                acceptable_pressure_range=acceptable_pressure_range,
                acceptable_humidity_range=acceptable_humidity_range)
        except ValueError:
            return render_template("calculator.html", \
                acceptable_temperature_range=acceptable_temperature_range, 
                acceptable_pressure_range=acceptable_pressure_range,
                acceptable_humidity_range=acceptable_humidity_range)
        except TypeError:
            return render_template("calculator.html", high_humidity=high_humidity)
        return render_template("calculator.html", \
            density=round(density,4),
            saturation_pressure=round(saturation_pressure, 4),
            humidity_absolute_converted=round(humidity_absolute_converted,4),
            relative_humidity=round(relative_humidity,2))
        
    else:
        return render_template("calculator.html")

@application.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)


@application.errorhandler(500)
def server_error(error):
    return render_template("500.html", error=error)

if __name__ == '__main__':
    application.run()

