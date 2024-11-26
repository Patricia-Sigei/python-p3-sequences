def print_fibonacci(length):
    fib_sequence = [0, 1]

    if length <= 0:
        print([])  
        return

    if length == 1:
        print([0])  
        return

    for i in range(2, length):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    print(fib_sequence)
