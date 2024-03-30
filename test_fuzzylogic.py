"""
Authors: Gaici Lin, Gia Ky Huynh
"""

import pytest
from fuzzylogic import get_fuzzy_output

"""
    wind["gentle"] =        [0, 0, 20]
    wind["moderate"] =      [19, 31, 41]
    wind["strong"] =        [39, 44, 49]

    snow["light"] =         [0, 0, 76.2] # up to 3 inches
    snow["moderate"] =      [50.8, 101.6, 152.4] # Starts at 2 inches, ends at 6 inches
    snow["heavy"] =         [101.6, 152.4, 200]  # beyond 6 inches
    snow["very heavy"] =    [152.4, 176.2, 200]
"""


def test_normal_case():
    # Normal case should not raise any exceptions and should return a str
    result = get_fuzzy_output(12.55, 23.4)
    assert isinstance(result, str), "The result should be a str"


def test_light_snow_and_gentle_wind_return_low_risk():
    result = get_fuzzy_output(12.55, 13.4)
    assert result == "Low"


def test_moderate_snow_and_gentle_wind_return_medium_risk():
    result = get_fuzzy_output(10, 93.4)
    assert result == "Medium"


def test_light_snow_and_moderate_wind_return_medium_risk():
    result = get_fuzzy_output(24, 13.4)
    assert result == "Medium"


def test_moderate_snow_and_moderate_wind_return_medium_risk():
    result = get_fuzzy_output(24, 93.4)
    assert result == "Medium"


def test_heavy_snow_or_strong_wind_return_high_risk():
    result = get_fuzzy_output(48, 10)
    assert result == "High"

    result = get_fuzzy_output(10, 150)
    assert result == "High"


def test_very_heavy_snow_return_high_risk():
    result = get_fuzzy_output(10, 180)
    assert result == "High"


def test_inputs_are_int():
    # Testing the integer inputs, should return a str
    result = get_fuzzy_output(48, 199)
    assert isinstance(result, str), "The result should be a str"


def test_negative_inputs():
    # Should raise ValueError for negative inputs
    with pytest.raises(ValueError):
        get_fuzzy_output(-1, -5)


def test_wind_speed_negative_and_snow_precipitation_positive_input():
    # Should raise ValueError for negative inputs
    with pytest.raises(ValueError):
        get_fuzzy_output(-1, 0)


def test_wind_speed_positive_and_snow_precipitation_negative_input():
    # Should raise ValueError for negative inputs
    with pytest.raises(ValueError):
        get_fuzzy_output(10, -5)


def test_zero_inputs():
    # Should raise ValueError for negative inputs
    with pytest.raises(ValueError):
        get_fuzzy_output(0, 0)


def test_wind_speed_zero_and_snow_precipitation_positive_input():
    # Should raise ValueError for negative inputs
    with pytest.raises(ValueError):
        get_fuzzy_output(0, 5)


def test_wind_speed_positive_and_snow_precipitation_zero_input():
    # Should raise ValueError for negative inputs
    with pytest.raises(ValueError):
        get_fuzzy_output(5, 0)


def test_inputs_are_none():
    # Should raise ValueError when inputs are None
    with pytest.raises(ValueError):
        get_fuzzy_output(None, None)


def test_inputs_out_of_range():
    # Should raise ValueError for out of range inputs
    with pytest.raises(ValueError):
        get_fuzzy_output(50, 201)
