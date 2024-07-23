def combine_lists(list1, list2):
    combined_list = list1 + list2
    return combined_list

def get_user_input(prompt):
    user_input = input(prompt)
    numbers = list(map(int, user_input.split()))
    return numbers

list1 = get_user_input("Enter numbers for the first list separated by spaces: ")
list2 = get_user_input("Enter numbers for the second list separated by spaces: ")

combined_list = combine_lists(list1, list2)
print(f"The combined list is: {combined_list}")
