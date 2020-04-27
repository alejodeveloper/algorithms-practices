BEGIN_OF_ITERATION = 5


def is_prime(my_number: int) -> bool:
    """
    Check if a number is prime or not trough the solution of a math series
    :param my_number: The number to evaluate if is prime or not
    :return: Bool that indicates if the number is priume or not
    """

    if my_number <= 1:
        return False

    elif my_number <= 3:
        return True

    elif my_number % 2 == 0 or my_number % 3 == 0:
        return False

    iteration_number = BEGIN_OF_ITERATION
    while iteration_number * iteration_number <= my_number:
        if my_number % iteration_number == 0 or my_number % (iteration_number + 2) == 0:
            return False
        iteration_number = iteration_number + 6
    return True


for _ in range(int(input())):
    number = int(input())
    prime = is_prime(number)
    my_str = 'Prime' if prime else 'Not prime'
    print(my_str)
