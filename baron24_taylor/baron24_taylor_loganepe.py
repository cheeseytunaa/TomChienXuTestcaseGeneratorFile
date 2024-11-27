from case_generator import CaseGenerator
from random import (
  randint as r,
  choice as c,
  uniform as u
)

class baron24_taylor_loganepe(CaseGenerator):
  def input_generator(self, case_index: int) -> str:
    x = u(-1, 1)
    n = r(60, 80)
    return f"{x} {n}"

  def algorithm(self, input_string: str) -> str:
    x, n = map(float, input_string.split())
    
    result = x
    temp = x
    
    for i in range(2, int(n) + 1):
      temp *= -1 * x * (i - 1) / i
      result += temp

    return f"{result:.8f}"

baron24_taylor_loganepe(number_of_testcases=20).generate(True)