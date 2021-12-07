"""
Author: Kateryna Trofymenko
Source: Exercise 3 from 01_reliability.pdf

Explained in README:
https://github.com/ekaterinatrofa/BSI_calculator/blob/master/README.md#exercise-3
"""

import task_solvers


def run():
    print("Exercise 3 from file 01_reliability.pdf:")

    failure_rate = float(input("Enter the failure rate per hour: "))
    hours_of_service = int(input("Enter the number of hours of service: "))
    reliability = task_solvers.calculate_reliability(failure_rate, hours_of_service)
    print()
    print(f'The calculated reliability is equal to {reliability:.4f} or {(reliability * 100):.2f}%.')
    print()

