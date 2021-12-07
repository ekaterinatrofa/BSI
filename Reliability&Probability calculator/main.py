"""
Author: Kateryna Trofymenko

"""


import reliability_of_the_hybrid_system
import reliability_for_the_compressor
import failure_rate_for_a_product
import reliability_and_reliability_function
import probability_of_the_equipment

if __name__ == "__main__":
    while True:
        print("1 - Calculate the operational reliability of continuous service")
        print("2 - Calculate the highest failure rate for a product")
        print("3 - Find the reliability and the reliability function")
        print("4 - Calculate the probability")
        print("5 - Calculate the reliability for hybrid connected components")
        print("0 - exit")
        choice = input("What would you like to do? ")
        print()
        if choice == "1":
            reliability_for_the_compressor.run()
        elif choice == "2":
            failure_rate_for_a_product.run()
        elif choice == "3":
            reliability_and_reliability_function.run()
        elif choice == "4":
            probability_of_the_equipment.run()
        elif choice == "5":
            reliability_of_the_hybrid_system.run()
        elif choice == "0":
            break
