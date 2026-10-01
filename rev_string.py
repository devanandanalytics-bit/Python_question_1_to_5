# 1. Reverse the string using for loop.



def reverse_string(input_string: str) ->str:
    """
       This function is reverse the user given string.
       Args :w
             input_str(str) : The string to be reverse
       Returns :
              str: The reverse version of input
       Raises:
              TyprError : If input is not a string
    """
    #Validate the input type 
    if not isinstance(input_string,str):
        raise TypeError("Input must be string ")
    reverse_str = ""
    for char in input_string:
        reverse_str = char + reverse_str
    return reverse_str

#-------main Execution-------  
if __name__ == "__main__":
    try:
        # taking input from user
        user_input = input("Enter your string to revesre: ")
        # calling the function
        result = reverse_string(user_input)
        # Display the reverse string 
        print(f"Reverse string {result}")
    except TypeError as e:
         print(e)
    except Exception as e:
         print(e)
