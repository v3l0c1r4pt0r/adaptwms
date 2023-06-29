import pytest
from adaptwms.translator import Translator

class TestTranslator:

  @pytest.mark.parametrize("test_input,expected", [
      # Świnoujście
      ((282855, 168533, 19), (1583087.292649083,7155270.217028664,1583163.7296773603,7155346.654056941)),
      ((141427, 84266, 18), (1583010.8556208059,7155270.217028664,1583163.7296773603,7155423.091085219)),
      ((70713, 42133, 17), (1582857.9815642515,7155117.34297211,1583163.7296773603,7155423.091085219)),

      # Ustrzyki Górne
      ((295129, 179815, 19), (2521275.377723432,6292907.664005297,2521351.8147517093,6292984.101033574)),
      ((147564, 89907, 18), (2521198.940695155,6292907.664005297,2521351.8147517093,6293060.538061852)),
      ((73782, 44953, 17), (2521198.940695155,6292907.664005297,2521504.6888082637,6293213.412118406)),
  ])
  def test_slippy2bbox(self, test_input, expected):
    translator = Translator()
    exp_left, exp_top, exp_right, exp_bottom = expected

    actual = translator.slippy2bbox(*test_input)
    act_left, act_top, act_right, act_bottom = actual

    assert act_left == pytest.approx(exp_left)
    assert act_top == pytest.approx(exp_top)
    assert act_right == pytest.approx(exp_right)
    assert act_bottom == pytest.approx(exp_bottom)
