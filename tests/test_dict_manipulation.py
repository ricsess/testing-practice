
import pytest
from src.dict_manipulation import switch_tuple_values


class TestSwitchTupleValues(object):
    def test_normal_values(self):
        arg = [(3, 4), (7, 6)]
        result = switch_tuple_values(arg)
        expected = [(4, 3), (6, 7)]
        assert result == expected

        arg = [(-6, 8), (0, 0), (100,1000)]
        result = switch_tuple_values(arg)
        expected = [(8, -6), (0, 0), (1000,100)]
        assert result == expected

        arg = [('big', 8), (0, 'small'), ('medium', 'medium')]
        result = switch_tuple_values(arg)
        expected = [(8, 'big'), ('small', 0), ('medium', 'medium')]
        assert result == expected

    def test_is_list(self):
        with pytest.raises(TypeError) as error_msg:
            arg = 'Bug'
            result = switch_tuple_values(arg)

        assert error_msg.match('arg must be a list')

    def test_each_element_is_tuple(self):
        with pytest.raises(TypeError) as error_msg:
            arg = [(5, 6), 'Not A Tuple', (1, 3, 4)]
            result = switch_tuple_values(arg)

        assert error_msg.match('all elements must be tuples')

    def test_each_tuple_is_length_2(self):
        with pytest.raises(ValueError) as error_msg:
            arg = [(1,2), (8,9), (60,40), (5,76,100)]
            result = switch_tuple_values(arg)

        assert error_msg.match('all tuples must have length 2')
