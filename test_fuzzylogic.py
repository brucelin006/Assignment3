import pytest
from fuzzylogic import get_fuzzy_output


def test_normal_case():
    # Normal case should not raise any exceptions and should return a float
    result = get_fuzzy_output(12.55, 23.4)
    assert isinstance(result, str), "The result should be a str"


def test_inputs_are_int():
    # Testing the integer inputs, should return a float
    result = get_fuzzy_output(48, 199)
    assert isinstance(result, str), "The result should be a str"


def test_negative_inputs():
    # Should raise ValueError for negative inputs
    with pytest.raises(ValueError):
        get_fuzzy_output(-1, -5)


def test_zero_inputs():
    # Should raise ValueError for negative inputs
    with pytest.raises(ValueError):
        get_fuzzy_output(0, 0)


def test_inputs_are_none():
    # Should raise ValueError when inputs are None
    with pytest.raises(ValueError):
        get_fuzzy_output(None, None)


def test_inputs_out_of_range():
    # Should raise ValueError for out of range inputs
    with pytest.raises(ValueError):
        get_fuzzy_output(50, 201)
