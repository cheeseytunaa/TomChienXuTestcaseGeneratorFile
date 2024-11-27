from random import randint as r
from case_generator import CaseGenerator

class vnuhn_hus_midterm_1_matrix_12(CaseGenerator):
  def __init__(self) -> None:
    super().__init__(number_of_testcases=20)

  def input_generator(self, index):
    n = r(20, 100)

    string = f"{n}\n"

    for _ in range(n):
      for _ in range(n):
        string += f"{r(10, 10**3)} "
      string += "\n"

    return string

  def algorithm(self, input_string):
    input_string = input_string.split("\n")
    return "\n".join(input_string[1:])

vnuhn_hus_midterm_1_matrix_12().generate(True)