"""
Author: Kateryna Trofymenko
Source: Exercise 4 from 01_reliability.pdf

Explained in README:
https://github.com/ekaterinatrofa/BSI_calculator/blob/master/README.md#exercise-4
"""
import task_solvers


def run():
    print("Exercise 4 from file 01_reliability.pdf:")

    reliability = int(input("Enter the reliability in %: "))
    reliability_converted = reliability/100
    hours = int(input("Enter the number of hours: "))
    highest_failure_rate = task_solvers.calculate_the_highest_failure_rate(reliability_converted, hours)
    print()
    print(f'The failure rate must be no higher than {highest_failure_rate:.8f} (failures per hour).')
    print()

