from random import randint as r
from case_generator import CaseGenerator

input_1 = """7 2
12 32 41 55 17 8 9"""

input_2 = """5 3
21 63 80 10 10"""

class vnuhn_hus_midterm_1_array_2(CaseGenerator):
  def __init__(self) -> None:
    super().__init__(number_of_testcases=20)

  def input_generator(self, index):
    if index == 1:
      return input_1
    elif index == 2:
      return input_2

    n = r(20, 100)
    string = f"{n} "
    
    if index % 3 == 0:
      k = 100000
      string += f"{k}\n"

      string += " ".join(map(str, [r(10, 10**3)] * n))
    else:
      k = r(1, 20)
      string += f"{k}\n"
      
      for _ in range(n):
        string += f"{r(10, 10**3)} "

    return string
  
  def algorithm(self, input_string):
    input_string = input_string.split("\n")

    n, k = map(int, input_string[0].split())
    array = list(map(int, input_string[1].split()))
    
    if k > len(array):
      return 2**31 - 1

    array_sorted = sorted(list(set(array)))

    try:
      return array_sorted[k - 1]
    except:
      return 2**31 - 1

vnuhn_hus_midterm_1_array_2().generate(True)