"""
Test File for airproperties app using pytesttest
David Burnett

.pylintrc disable=redefined-outer-name,no-value-for-parameter
"""

# import imp
from multiprocessing.connection import Client
import pytest
# from airproperties import main
import main_airproperties
from airproperties import app as flask_app
import air_properties_data


def test_calculate_air_density():
    """
    Test air density function
    """
    assert round(main_airproperties.calculate_air_density(59, 14.7), 4) == 0.0765
    
    with pytest.raises(ValueError):
        main_airproperties.calculate_air_density(59 , 7001)

    with pytest.raises(ValueError):
        main_airproperties.calculate_air_density(59 , -1)

    with pytest.raises(ValueError):
        main_airproperties.calculate_air_density(570 , 14.7)

    with pytest.raises(ValueError):
        main_airproperties.calculate_air_density(-50 , 14.7)



def test_convert_humidity_absolute():
    """
    Test humidity conversion function
    """
    assert round(main_airproperties.convert_humidity_absolute(21.6),4) == 0.0031 
    
    with pytest.raises(ValueError):
        main_airproperties.convert_humidity_absolute(201)
    
    with pytest.raises(ValueError):
        main_airproperties.convert_humidity_absolute(-1)


def test_get_saturation_pressure():
    """
    Test saturation pressure function
    """
    saturation_pressure_data_test = [[60,0.2563],[70,0.3632]]

    assert round(main_airproperties.get_saturation_pressure(saturation_pressure_data_test, 60), 4) == 0.2563
    assert round(main_airproperties.get_saturation_pressure(saturation_pressure_data_test, 65),4) == 0.3098

    with pytest.raises(ZeroDivisionError):
        main_airproperties.get_saturation_pressure(saturation_pressure_data_test, 560)

    with pytest.raises(ZeroDivisionError):
        main_airproperties.get_saturation_pressure(saturation_pressure_data_test, -50)


def test_calculate_relative_humidity():
    """
    Test relative humidity function
    """

    assert round(main_airproperties.calculate_relative_humidity(0.0031, 14.7, .2485) ,2) == 0.29

    assert main_airproperties.calculate_relative_humidity(0.0286, 14.7, .2485) == None

    with pytest.raises(ValueError):
        main_airproperties.calculate_relative_humidity(0.0031, 7001, .2485)

    with pytest.raises(ValueError):
        main_airproperties.calculate_relative_humidity(0.0031, -1, .2485)


""" Testing Flask App """

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    return app.test_client()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    expected = 'Flask Moist Air Properties Calculator'
    assert b'Flask Moist Air Properties Calculator' in response.data



