def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(lst):
    prime_count = 0
    for num in lst:
        if is_prime(num):
            prime_count += 1
    return prime_count

def get_user_input():
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    return numbers

numbers = get_user_input()
prime_count = count_primes(numbers)
print(f"The number of prime numbers in the list is: {prime_count}")
