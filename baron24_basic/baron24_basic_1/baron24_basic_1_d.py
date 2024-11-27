from case_generator import CaseGenerator
from random import (
  randint as r,
  choice as c,
  uniform as u
)

class baron24_basic_1_d(CaseGenerator):
  def input_generator(self, case_index: int) -> str:
    a = lambda: r(-10**9, 10**9)
    return "%s %s" % (a(), a())

  def algorithm(self, input_string: str) -> str:
    a, b = map(int, input_string.split(" "))
    return f"{a} + {b} = {a + b}"

baron24_basic_1_d(number_of_testcases=50).generate(True)