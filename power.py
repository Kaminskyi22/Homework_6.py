def power_list_elements(lst, power):
    powered_list = [num ** power for num in lst]
    return powered_list

def get_user_input():
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    return numbers


numbers = get_user_input()
power = int(input("Enter the power value: "))

powered_list = power_list_elements(numbers, power)
print(f"The list with elements raised to the power of {power} is: {powered_list}")
