
import pytest
from src.utils import square_plus_one, replace_spaces


class TestSquarePlusOne(object):
    def test_boundary_value(self):
        result = square_plus_one(2)
        assert (result == 5)

    def test_normal_values(self):
        result = square_plus_one(3)
        assert (result == 10)

        result = square_plus_one(5)
        assert (result == 26)

        result = square_plus_one(10)
        assert (result == 101)

    def test_non_int(self):
        with pytest.raises(TypeError) as error_msg:
            result = square_plus_one(5.5)

        assert error_msg.match('x must be int')

    def test_smaller_than_expected(self):
        with pytest.raises(ValueError) as error_msg:
            result = square_plus_one(1)

        assert error_msg.match('x must be greater than one')


class TestReplaceSpaces(object):
    def test_normal_values(self):
        result = replace_spaces('Big Apple')
        assert (result == 'Big_Apple')

        result = replace_spaces('Chubby monster_mother spider')
        assert (result == 'Chubby_monster_mother_spider')

    def test_non_str(self):
        with pytest.raises(TypeError) as error_msg:
            result = replace_spaces(100)

        assert error_msg.match('s must be string')
