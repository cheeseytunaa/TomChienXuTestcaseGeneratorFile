from case_generator import CaseGenerator
from random import (
  randint as r,
  choice as c,
  uniform as u
)

class baron24_basic_1_a(CaseGenerator):
  def input_generator(self, case_index: int) -> str:
    a = lambda: r(-1000, 1000)
    return "%s %s %s" % (a(), a(), a())

  def algorithm(self, input_string: str) -> str:
    return str(sum(map(int, input_string.split())))

baron24_basic_1_a(number_of_testcases=50).generate(True)