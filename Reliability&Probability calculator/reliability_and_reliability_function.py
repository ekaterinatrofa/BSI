"""
Author: Kateryna Trofymenko
Source: Exercise 5 from 01_reliability.pdf

Explained in README:
https://github.com/ekaterinatrofa/BSI_calculator/blob/master/README.md#exercise-5

"""
import task_solvers


def run():
    print("Exercise 5 from file 01_reliability.pdf:")

    print("Let's solve part a of the Exercise ")

    mtbf = int(input("Enter the mean time between failures (in hours): "))

    failure_rate = task_solvers.calculate_failure_rate(mtbf)
    print()
    print(f'The failure rate is {failure_rate:.2f} (failures per hour).')
    print()
    task_solvers.print_reliability_function(failure_rate)

    print("Let's solve part 'b' of the Exercise ")

    hours = int(input("Enter the number of hours: "))

    reliability = task_solvers.calculate_reliability(failure_rate, hours)
    print()
    print(f'The calculated reliability is equal to {reliability:.4f} or {(reliability * 100):.2f}%.')
    print()
