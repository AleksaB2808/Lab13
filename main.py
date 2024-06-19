import math
import re
import statistics

def interpolate_missing(values):
    result = []
    prev_val = None
    consecutive_nones = 0

    for val in values:
        if val is not None:
            if prev_val is not None:
                if consecutive_nones > 0:
                    step = (val - prev_val) / (consecutive_nones + 1)
                    interpolated_values = [round(prev_val + i * step) for i in range(1, consecutive_nones + 1)]
                    result.extend(interpolated_values)
                    consecutive_nones = 0
            result.append(val)
            prev_val = val
        else:
            if prev_val is not None:
                consecutive_nones += 1

    return result


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def process_batches(data, batch_size):
    batches = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]
    return [max(batch) for batch in batches]


def encode_string(string):
    if not string:
        return ""

    encoded = ''
    prev_char = string[0]  
    count = 1

    for char in string[1:]:  
        if char != prev_char:
            if count > 1:
                encoded += str(count)
            encoded += prev_char
            count = 1
            prev_char = char
        else:
            count += 1

    if count > 1:
        encoded += str(count)
    encoded += prev_char

    return encoded


def decode_string(encoded):
    decoded = ''
    count = ''
    for char in encoded:
        if char.isdigit():
            count += char
        else:
            if count == '':
                decoded += char
            else:
                decoded += char * int(count)
                count = ''
    return decoded



def rotate_matrix(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = matrix[i][j]

    return rotated


def regex_search(strings, pattern):
    return [string for string in strings if re.search(pattern, string)]


def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    merged.extend(arr1[i:])
    merged.extend(arr2[j:])

    return merged


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def group_by_key(data, key):
    grouped = {}
    for item in data:
        if item[key] not in grouped:
            grouped[item[key]] = []
        grouped[item[key]].append(item['value'])
    return grouped


def remove_outliers(lst):
    if len(lst) < 2:
        return lst 

    mean = statistics.mean(lst)
    stdev = statistics.pstdev(lst)
    lower_bound = mean - 2 * stdev
    upper_bound = mean + 2 * stdev

    filtered_lst = []

    for x in lst:
        if lower_bound < x < upper_bound:
            filtered_lst.append(x)

    return filtered_lst

