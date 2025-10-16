from langchain_core.tools import tool

@tool
def convert_length_inches_to_cm(inches_length: int) -> int:
    """
    Converts a given length from inches to centimeters.

    This function takes a length measurement in inches and converts it to centimeters
    using the conversion factor of 2.54. The resulting value is rounded to the nearest
    integer and returned.

    :param inches_length: The length in inches to be converted
    :type inches_length: int
    :return: The length converted to centimeters, rounded to the nearest integer
    :rtype: int
    """
    return round(inches_length * 2.54)

@tool
def convert_weight_cups_to_grams(cups_weight: float) -> int:
    """
    Converts weight from cups to grams. This function accepts a weight in cups and
    returns the equivalent weight in grams. It assumes a standard conversion
    rate of 1 cup = 250 grams.

    :param cups_weight: The weight in cups
    :type cups_weight: float
    :return: The equivalent weight in grams
    :rtype: int
    """
    return round(cups_weight * 250)

@tool
def convert_volume_cups_to_millilitres(cups_volume: float) -> int:
    """
    This function takes a floating-point value representing the volume in cups
    and converts it into millilitres by multiplying with a conversion factor of 240.
    The result is rounded to the nearest integer to ensure accurate representation
    of the millilitres value.

    :param cups_volume: The volume in cups to be converted.
    :type cups_volume: float
    :return: The equivalent volume in ml.
    :rtype: int
    """
    return round(cups_volume * 240)
