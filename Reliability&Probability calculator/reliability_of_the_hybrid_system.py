"""
Author: Kateryna Trofymenko
Source: Exercise 5 from Selected_Problems_And_Answers.pdf (Problem Set for Chapter 4)

Explained in README: https://github.com/ekaterinatrofa/BSI_calculator/blob/master/README.md#03_problem-set-for-chapter-4pdf
"""

import task_solvers


def run():
    print("Exercise 5 from problem set for chapter 4 file 03.pdf :")

    Rd = float(input("Enter the reliability for D component: "))
    Re = float(input("Enter the reliability for E component: "))

    reliability_series = task_solvers.calculate_reliability_for_two_series_connected_components(Rd, Re)
    print(f'The calculated reliability for series connected components is equal to {reliability_series}')

    Ra = float(input("Enter the reliability for A component: "))
    Rb = float(input("Enter the reliability for B component: "))
    Rc = float(input("Enter the reliability for C component: "))

    reliability_parallel = task_solvers.calculate_reliability_for_three_parallel_connected_components(Ra, Rb, Rc)
    print(f'The calculated reliability for three parallel connected A, B, C components is equal '
          f'to {reliability_parallel}')
    print()
    reliability = task_solvers.calculate_total_system_reliability(reliability_series, reliability_parallel)
    print(f'The calculated reliability for the whole system is equal to {reliability}')
    print()
