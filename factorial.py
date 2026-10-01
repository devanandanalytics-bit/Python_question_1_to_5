# 5. Calculate factorial of a number
# Write a function calculate_factorial that takes a number as input and returns its factorial. Handle cases where the input is not a non-
# negative integer or zero.
# Example: If number is 5 factorials will be (5x4x2x3x2x1=120)
# Expected output: 120 if number is 5


def factorial_finder(number: int) ->int:
    """
        The Function return factorial given user number.

        Args:
             number(int): Number should be integer

        Return:
              int: factorial return int number

        Raise:
              TypeError : Number should be integer
              ValueError: if number is negative 
    """
    # validate the input 
    if isinstance(number,bool):
        raise TypeError("Boolean value is not allows :")
        # check type of number 
    if not isinstance(number,int):
            raise TypeError("Number should be integer :")
    if number < 0:
        raise ValueError("Negative number is not allows :")


    factorial = 1
    for i in range(1,number+1):
        factorial = factorial * i
    return factorial    


#main execution
if __name__ == "__main__":
    try:
        # taking input
        user_input = input("Enter your number to find factorial : ")
        # converting the integer
        user_input = int(user_input)
        print("factorial :",factorial_finder(user_input))
    except ValueError as e:
        print(e)
    except TypeError as e:
        print("Error",e)
    except Exception as e:
        print(e)

