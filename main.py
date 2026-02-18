#!/usr/bin/env python3

def largest_of_3(numbers):
    ln = 0
    nln = 0
    a = 0
    b = 0
    c = 0

    for n in numbers:
        if n < ln:
            nln = ln
            ln = n
        elif n < nln:
            nln = n
        elif n > a:
            c = b
            b = a
            a = n
        elif n > b:
            c = b
            b = n
        elif n > c:
            c = n

    if (ln * nln * a) > a * b * c:
        return [ln, nln, a]
    else:
        return [c, b, a]


def water_bucket_volume(numbers):
    total = 0
    start = 0
    end = 0

    while start < len(numbers) - 1:
        if numbers[start + 1] < numbers[start]:
            end = start + 1

            # find next highest bar
            for i in range(start + 1, len(numbers)):
                if numbers[i] > numbers[end]:
                    end = i

            ceiling = numbers[start]
            if (numbers[end]) < ceiling:
                ceiling = numbers[end]

            for i in range(start + 1, end):
                if (numbers[i] < ceiling):
                    total += ceiling - numbers[i]

            start = end
        else:
            start += 1

    return total


if __name__ == "__main__":
    numbers = [-1, 2, 0, 6, 8]

    ret = largest_of_3(numbers)
    assert(ret == [2, 6, 8])

    numbers = [7, 9, -12, -7, 9]
    ret = largest_of_3(numbers)
    assert(ret == [-12, -7, 9])

    numbers = [-10, -9, 0, 1]
    ret = largest_of_3(numbers)
    assert(ret == [-10, -9, 1])

    numbers = [0, -10, -1, 1, 9]
    ret = largest_of_3(numbers)
    assert(ret == [-10, -1, 9])

    numbers = [0, -9, -1, 1, 9]
    ret = largest_of_3(numbers)
    assert(ret == [-9, -1, 9])

    numbers = [4, 2, 0, 1, 3, 2, 1, 4]
    ret = water_bucket_volume(numbers)
    assert(ret == 15)

    numbers = [4, 0, 1, 2]
    ret = water_bucket_volume(numbers)
    assert(ret == 3)

    numbers = [1, 2, 4, 3, 3, 5, 0, 1, 0, 2, 1, 0]
    ret = water_bucket_volume(numbers)
    assert(ret == 7)

    numbers = [1, 3, 5, 3, 1, 2, 1, 0, 2, 1, 0]
    ret = water_bucket_volume(numbers)
    assert(ret == 4)

    numbers = [0, 1, 3, 1, 2, 1, 0, 1, 0]
    ret = water_bucket_volume(numbers)
    assert(ret == 2)

