def multiply_list_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def get_user_input():
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    return numbers

numbers = get_user_input()
product = multiply_list_elements(numbers)
print(f"The product of the entered numbers is: {product}")
