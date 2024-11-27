from random import (
  randint as r,
  choice as c
)
from case_generator import CaseGenerator

input_1 = """3 2
1 2 3
4 5 6
7 8 28"""

input_2 = """2 0
1 2
3 4"""

class vnuhn_hus_midterm_1_matrix_4(CaseGenerator):
  def __init__(self) -> None:
    super().__init__(number_of_testcases=20)

  @staticmethod
  def matrix_generator(n):
    string = ""
    
    for _ in range(n):
      for _ in range(n):
        string += f"{r(10, 10**3)} "
      string.strip(" ")
      string += "\n"

    return string.strip("\n")

  @staticmethod
  def string_to_matrix(string):
    return [list(map(int, line.strip().split())) for line in string.split("\n")]

  @staticmethod
  def matrix_to_string(matrix):
    return '\n'.join([' '.join(map(str, line)) for line in matrix])

  def input_generator(self, index):
    if index == 1:
      return input_1
    elif index == 2:
      return input_2

    n = r(4, 20)

    matrix = self.matrix_generator(n)

    if index % 4 == 0:
      matrix = self.string_to_matrix(matrix)

      for _ in range(r(1, n**2 // 3)):
        matrix[r(0, n - 1)][r(0, n - 1)] = c([6, 28, 496, 8128, 33550336])

      matrix = self.matrix_to_string(matrix)

    k = r(0, n - 1)
    input_matrix = f"{n} {k}\n"
    input_matrix += matrix

    return input_matrix

  @staticmethod
  def is_perfect_number(number):
    sum_of_divisors = 0

    for i in range(1, number):
      if number % i == 0:
        sum_of_divisors += i

    return number == sum_of_divisors

  def algorithm(self, input_string):
    input_string = input_string.split("\n")

    result = ""

    n, k = map(int, input_string[0].split())
    matrix = [list(map(int, line.split())) for line in input_string[1:]]


    for line in matrix:
      if self.is_perfect_number(line[k]):
        result += f"{line[k]} "

    return result or "Unavailable."

vnuhn_hus_midterm_1_matrix_4().generate(True)