# def prime_sum(n):
#     # Check if n is less than 2
#     if n < 2:
#         return -1

#     # Check if n is prime
#     is_prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#             break

#     # If n is not prime, return -1
#     if not is_prime:
#         return -1

#     # If n is prime, calculate the sum of all numbers from 0 to n
#     total_sum = sum(range(n+1))

#     # Return the total sum
#     return total_sum


# print(prime_sum(5))  # Output: 15 (0 + 1 + 2 + 3 + 4 + 5)
# print(prime_sum(10))  # Output: -1
# check the prime number

# check the sum of the numbers from the prime numbers
def is_prime(n):
    if n < 2:
        return -1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return -1
    return n


print(is_prime(5))  # Output: 5
print(is_prime(10))  # Output: -1
