def fibonacci_numbers():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    sum = 0
    fibonacci_generator = fibonacci_numbers()
    fibonacci_number = fibonacci_generator.next()
    while fibonacci_number <= 4000000:
        if fibonacci_number % 2 is 0:
            sum += fibonacci_number
        fibonacci_number = fibonacci_generator.next()

    print 'Answer: %s' % sum