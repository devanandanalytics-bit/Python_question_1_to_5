
# 2. Find the Largest Element in a List using for loop.
# Write a function to find the largest element in a list without using built-in sorting.
# Example
# Input: [7, 5, 8, 2, 10, 9]
# Expected Output: 10
# Example
# Input: [4, 4, 4, 4]
# Expected Output: None



def find_largest_number(numbers_list: list[float]) -> float:
    """
       Function to find largest number in the list.

       Args: 
           number_list(number_list: list[float]): A list contain numberic value (int or float)

       Return:
             float: The largest number in the list.

        Raises:
              TypeError: If input is not a list or contains non-numberic values.
              ValueError: If the list is Empty.

    """



    # validate that input is a list
    if not isinstance(numbers_list, list):
        raise TypeError("Input must be a list of number float or int")

    # validate that list is empty
    if not numbers_list:
        raise ValueError("List cannot be empty")

    # validate that list elements should be numeric
    for num in numbers_list:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements must be numeric")

    largest = numbers_list[0]

    for num in numbers_list:
        if num > largest:
            largest = num

    return largest


# Main Execution
if __name__ == "__main__":
    try:
        numbers_list = [1,2,3,4,45,5,6,7]
        result = find_largest_number(numbers_list)
        print("Largest number in the list is:", result)

    except (TypeError, ValueError) as error:
        print(error)

    except Exception as e:
        print(e)