######################
# Positional Arguments
######################

param_args = [1, 2, 3]
param_kwargs = {'x': 1, 'y': 2}

def func(a, b=1):
    print(a, b)

def positional_unlimited(a, b=1, *args):
    print(a, b, *args)

func(1)
func(1, 42)
func(1, 2, 3)  # Noncompliant. Too many positional arguments
func()  # Noncompliant. Missing positional argument for "a"

positional_unlimited(1, 2, 3, 4, 5)

def positional_limited(a, *, b=2):
    print(a, b)

positional_limited(1, 2)  # Noncompliant. Too many positional arguments