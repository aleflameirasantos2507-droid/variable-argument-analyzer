from time import sleep


def analyze_values(*numbers):
    print('Analyzing the provided values...')

    count = 0
    largest = 0

    for number in numbers:
        print(number, end=' ')
        sleep(0.2)

        if count == 0:
            largest = number
        elif number > largest:
            largest = number

        count += 1

    print()
    print(f'You entered {count} value(s).')

    if count == 0:
        print('No values were provided.')
    else:
        print(f'The largest value is {largest}.')

    print('=' * 40)


analyze_values(5, 1, 2, 561, 515, 11, 1, 412)
analyze_values(4, 1, 5, 1, 51, 5, 1, 6, 2, 1, 5, 6, 14)
analyze_values(3, 2, 5, 1, 5, 6, 1, 2, 5, 1, 5, 1, 6, 11, 26, 78, 2, 6, 24)
analyze_values()
