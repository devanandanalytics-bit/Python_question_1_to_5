# 3. Take the input from user and find whether number is prime or not?
# Prime numbers are number which are divide by 1 or themselves only.
# Example: 13 is a prime number.
# Example: 97 is a prime number


def is_prime_number(number: int) ->bool:
    """
       Function to check whether a number is not a prime or not .
       Args:
            number(int):The number to check
       Return:
              bool: True if the number is not an integer.
       Raises:
             TypeError: If input is not an integer
             ValueError: If number is less then 2(since prime are >= 2.)
    """
    if not isinstance(number,int):
        raise TypeError("Input must be an integer")
    if number < 2:
        raise ValueError("Prime number are greater then or equal to 2")
#logic

    for i in range(2,int(number**.5)+1):
         if number % i == 0:
             return False
    else:
         return True
 #main Execution
if __name__ == "__main__":
    try:
        # taking input from user
        user_input = input("Enter the number to check prime or not :")
        # validate and convert input to integer
        if not user_input.strip().isdigit():
            raise TypeError("input must be digit(no letter no string not float")
        number = int(user_input)
        # calling function
        if is_prime_number(number):
            print(f"{number} is a prime number")

        else:
            print(f"{number} is not a prime number")
    except(TypeError,ValueError) as error:
        print(error)
    except Exception as e:
        print("something went wrong")
