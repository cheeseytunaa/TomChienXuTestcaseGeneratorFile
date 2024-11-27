from case_generator import CaseGenerator
from random import (
  randint as r,
  choice as c,
  uniform as u
)

class baron24_basic_1_b(CaseGenerator):
  def input_generator(self, case_index: int) -> str:
    a = lambda: r(0, 100)
    b = lambda: c([r(0, 100), 0])
    return "%s %s" % (a(), b())

  def algorithm(self, input_string: str) -> str:
    a, b = map(int, input_string.split(" "))
    result = ""

    result += f"{a + b}\n"
    result += f"{a - b}\n"
    result += f"{a * b}\n"
    result += f"{a / b:.2f}\n" if b != 0 else "ERROR\n"
    result += f"{a % b}" if b != 0 else "ERROR"
    
    return result

baron24_basic_1_b(number_of_testcases=50).generate(True)