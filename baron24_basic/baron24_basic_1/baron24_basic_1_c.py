from case_generator import CaseGenerator
from random import (
  randint as r,
  choice as c,
  uniform as u
)

class baron24_basic_1_c(CaseGenerator):
  def input_generator(self, case_index: int) -> str:
    r = lambda: u(0, 1000)
    return f"{r():.3f}"

  def algorithm(self, input_string: str) -> str:
    r = float(input_string)
    return f"{r * 2 * 3.14:.3f} {r * r * 3.14:.3f}"

baron24_basic_1_c(number_of_testcases=50).generate(True)