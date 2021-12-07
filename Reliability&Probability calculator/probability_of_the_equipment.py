"""
Author: Kateryna Trofymenko
Source: Exercise 6 from 01_reliability.pdf

Explained in README:
https://github.com/ekaterinatrofa/BSI_calculator/blob/master/README.md#exercise-6
"""

import task_solvers


def run():
    print("Exercise 6 from file 01_reliability.pdf:")

    mtbf = int(input("Enter the mean time between failures (in hours): "))
    hours = int(input("Enter the number of hours: "))

    failure_rate = task_solvers.calculate_failure_rate(mtbf)
    reliability = task_solvers.calculate_reliability(failure_rate, hours)
    print()
    print(f'The calculated reliability is equal to {reliability:.2f} or {(reliability * 100):.0f}%.')
    print()
