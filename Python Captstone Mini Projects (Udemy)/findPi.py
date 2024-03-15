from math import pi


def nth_pi(n=None):
    """
    Returns the value of pi rounded to the nth digit of accuracy.

    Args:
    - n (int): The number of decimal places for pi. If None, prompts the user for input.

    Returns:
    - str: The value of pi rounded to the nth digit of accuracy.
    """
        
    if n is None:
        while True:
            try:
                n = int(input("Enter the n'th Digit of accuracy: "))
                break
            except ValueError:
                print("Please enter a valid integer.")
                continue
    pi_val= f'{pi:.{n}f}'

    return pi_val

if __name__ == "__main__":
    print(nth_pi())
