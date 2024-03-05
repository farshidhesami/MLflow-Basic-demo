import sys

def get_float_arg(index, default=0.5):
    try:
        return float(sys.argv[index]) if len(sys.argv) > index else default
    except ValueError:
        print(f"Error: Argument {index} is not a valid number. Defaulting to {default}.")
        return default

alpha = get_float_arg(1)
l1_ratio = get_float_arg(2)

print(alpha, l1_ratio)





'''
# Simple code :

import sys 

alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5      
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

print(alpha, l1_ratio)

'''