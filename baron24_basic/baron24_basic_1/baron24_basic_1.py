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

class baron24_basic_1_c(CaseGenerator):
  def input_generator(self, case_index: int) -> str:
    r = lambda: u(0, 1000)
    return f"{r():.3f}"

  def algorithm(self, input_string: str) -> str:
    r = float(input_string)
    return f"{r * 2 * 3.14:.3f} {r * r * 3.14:.3f}"

class baron24_basic_1_d(CaseGenerator):
  def input_generator(self, case_index: int) -> str:
    a = lambda: r(-10**9, 10**9)
    return "%s %s" % (a(), a())

  def algorithm(self, input_string: str) -> str:
    a, b = map(int, input_string.split(" "))
    return f"{a} + {b} = {a + b}"

# baron24_basic_1_a(number_of_testcases=50).generate(True)
baron24_basic_1_b(number_of_testcases=50).generate(True)
# baron24_basic_1_c(number_of_testcases=50).generate(True)
# baron24_basic_1_d(number_of_testcases=50).generate(True)