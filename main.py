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
    bars = [0]
    next_highest = 0
    end_idx = 0

    for n in numbers:
        if n >= bars[0]:
            for j in range(1, len(bars)):
                total += bars[0] - bars[j]
            bars.clear()
            bars.append(n)
            next_highest = 0
            end_idx = 0
        else:
            bars.append(n)
            if n > next_highest:
                next_highest = n
                end_idx = len(bars)

    if next_highest > 0:
        for i in range(1, end_idx):
            total += next_highest - bars[i]

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

