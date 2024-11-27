from random import randint as r
from case_generator import CaseGenerator

input_1 = """3
1 2 3
4 5 6
7 8 9"""

class vnuhn_hus_midterm_1_matrix_3(CaseGenerator):
  def __init__(self) -> None:
    super().__init__(number_of_testcases=20)

  def input_generator(self, index):
    if index == 1:
      return input_1
    
    with open(f"problems/vnuhn_hus_midterm_1_matrix_12/testcase/{index}.in", "r") as file:
      return file.read()

  def algorithm(self, input_string):
    input_string = input_string.split("\n")

    n = int(input_string[0])
    matrix = [list(map(int, line.split())) for line in input_string[1:]]

    sum = 0
    for i in range(n):
      sum += matrix[i][n - 1 - i]

    return sum

vnuhn_hus_midterm_1_matrix_3().generate(True)