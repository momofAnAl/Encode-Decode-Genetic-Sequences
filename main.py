# Part 1 imports
from part_one import driver

# Part 2 imports
# from part_two import driver

if __name__ == "__main__":
    user_input = ""
    while user_input != "r" and user_input != "t":
        user_input = input('Please enter r to run or t to test => ')

    if user_input == "r":
        driver()
    else: 
        from sequence_tests import tests
        tests()
        
        
"""
Main.py calls test()> test() calls part_one_tests() > part_one_tests calls dna_test() > dna_tests() calls encode_strand()
"""