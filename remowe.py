def remove_element(lst, element_to_remove):
    initial_length = len(lst)
    lst = [num for num in lst if num != element_to_remove]
    removed_count = initial_length - len(lst)
    return removed_count, lst


def get_user_input():
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    return numbers


numbers = get_user_input()
element_to_remove = int(input("Enter the number to remove: "))
removed_count, updated_list = remove_element(numbers, element_to_remove)
print(f"Number of elements removed: {removed_count}")
print(f"Updated list: {updated_list}")
