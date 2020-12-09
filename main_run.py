import numpy as np
import math as math

from typing import Iterable
from typing import Optional
from typing import Dict


def t_list(all_name: Iterable[str]) -> int:
    for name in all_name:
        print("name is ", name)
    return 0


t_list(["phuvh", "afhjdgs", "lsfkhjds"])

a: int = 10
b = math.ceil(2.5)
print("hello world")
print("b is ", b)
c: int = 10 if a > b else 1
print("c is", c)
if a == 10:
    print("fsdhgj")
else:
    print("ghjdkgh")
for i in range(0, 3):  # giống vòng for, i chạy 0,1,2
    print("i is", i)


def dfwsf(e: int) -> int:
    return 5


"""
def g() -> None:
return 1 + 4
"""
