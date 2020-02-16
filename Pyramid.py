correct_pyramid = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]


def give_bigger(last_row, i):
    return last_row[i] if last_row[i] > last_row[i + 1] else last_row[i + 1]


def do_calc(target_row, last_row):
    for i in range(len(target_row)):
        target_row[i] += give_bigger(last_row, i)
    return target_row


def calculate_level(pyramid):
    pyramid[-2] = do_calc(pyramid[-2], pyramid[-1])
    return pyramid


def calculate_longest_slide(pyramid):
    if len(pyramid) == 1:
        return pyramid[0][0]
    while len(pyramid) > 1:
        pyramid = calculate_level(pyramid)
        del pyramid[-1]
    return pyramid[0][0]


def longest_slide_down(pyramid):
    if input_pyramid_is_correct(pyramid):
        return calculate_longest_slide(pyramid)
    else:
        raise Exception("The input pyramid is not correct.")


def input_pyramid_is_correct(pyramid):
    current_size = 1
    if type(pyramid) is tuple:
        return False
    for block in pyramid:
        if type(block) is list and len(block) == current_size:
            for elem in block:
                if number_check(elem) is False:
                    return False
            current_size = current_size + 1
        else:
            return False
    return True


def number_check(n):
    return True if type(n) is int else False


print(longest_slide_down(correct_pyramid))
