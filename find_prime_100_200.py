# 4. Find all Prime numbers between 100 and 200?
# All prime numbers between 100 and 200 are:
# 101, 103, 107, 109, 113,127, 131, 137, 139,149, 151, 157,163, 167,173, 179, 181,191, 193, 197, 199

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
    for i in range(2,int(number**.5)+1):
         if number % i == 0:
             return False
    else:
         return True
 #main Execution
if __name__ == "__main__":
    try:
        prime_number = []
        lower_limit = input("Enter lower limit :")
        upper_limit = input("Enter upper limit :")
        if not lower_limit.strip().isdigit():
            raise TypeError("Lower limit must be a validate integer (no decimal or not letter)")
        if not upper_limit.strip().isdigit():
            raise TypeError("upper limit must be a validate integer (no decimal or not letter)")
        lower_limit = int(lower_limit)
        upper_limit = int(upper_limit)

        for i in range(lower_limit,upper_limit):
            if is_prime_number(i):
                print(f"{i} prime number :")
                prime_number.append(i)
        print(prime_number)       
    except Exception as e:
        print(e)