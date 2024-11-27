from random import randint as r
from case_generator import CaseGenerator

class vnuhn_hus_midterm_1_array_1(CaseGenerator):
  def __init__(self) -> None:
    super().__init__(number_of_testcases=20)

  def input_generator(self, index):
    n = r(20, 100)
    string = f"{n}\n"
    
    if index % 2:
      u_1 = r(10**2, 10**4)
      d = r(10, 10**3)

      for i in range(n):
        string += f"{u_1 + i * d} "
    else:
      for i in range(n):
        string += f"{r(0, 10**5)} "

    return string
  
  def algorithm(self, input_string):
    input_string = input_string.split("\n")
    n = int(input_string[0])
    a = list(map(int, input_string[1].split()))
    
    d = a[1] - a[0]
    
    for i in range(1, n - 1):
      if a[i + 1] - a[i] != d:
        return "false"
    
    return "true"

vnuhn_hus_midterm_1_array_1().generate(True)