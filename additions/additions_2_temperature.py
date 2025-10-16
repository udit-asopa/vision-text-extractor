from langchain_core.tools import tool

@tool
def convert_temperature_fahrenheit_to_celsius(fahrenheit_temperature: int) -> int:
    """
    Convert a given temperature from Fahrenheit to Celsius.

    This function takes a temperature value in Fahrenheit and converts it into
    its equivalent in Celsius using the standard formula. The output temperature
    is rounded to the nearest integer.

    :param fahrenheit_temperature: The temperature in Fahrenheit to be converted.
    :type fahrenheit_temperature: int
    :return: The equivalent temperature in Celsius, rounded to the nearest integer.
    :rtype: int
    """
    return round((fahrenheit_temperature - 32) * 5 / 9)