# Calculate factorial from user provided integer and
# it's approximate using N^n e^-N SqrtN Sqrt2Pi

import math

def main():
    # Get integer input from user
    while True:
        integer = input("Enter integer to calculate from (between 1 and 150): ")
        if integer.isnumeric():
            # Input returns string, so this casts it to an integer
            integer = int(integer)
            if (integer > 0) and (integer < 151):
                break
            else:
                print("Number must be between 1 and 150")
        else:
            print("Please provide an integer")
    
    # Calculate the true factoral
    true_factorial = math.factorial(integer)
    scietific_notation = "{:e}".format(true_factorial)
    if true_factorial < 6402373705728001:
        print("The true number is:", true_factorial)
    else:
        print("In true number is:", scietific_notation)
    
    # Calculate the approximate factorial
    approximate = pow(integer, integer) * pow(math.e, -integer) * math.sqrt(integer) * math.sqrt(2 * math.pi)
    print ("The approximate number is: ", approximate)
    
    # Calculate the ratio of actual to approximate
    ratio = true_factorial / approximate
    print ("The ratio of actual to approximate is:", ratio)


if __name__ == "__main__":
    main()