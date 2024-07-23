def find_minimum(lst):
    if not lst:
        raise ValueError("The list is empty")
    
    minimum = lst[0]
    for num in lst:
        if num < minimum:
            minimum = num
    return minimum

def get_user_input():
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    return numbers

numbers = get_user_input()
min_value = find_minimum(numbers)
print(f"The minimum value in the list is: {min_value}")
