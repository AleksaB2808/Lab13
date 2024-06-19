# Lab13
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
Опис:
Ця функція генерує послідовність чисел Фібоначчі довжиною n. Використовується генератор для ефективної генерації значень без використання пам'яті на зберігання всіх значень одночасно.

Функція process_batches

def process_batches(data, batch_size):
    batches = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]
    return [max(batch) for batch in batches]
Опис:
Ця функція розділяє вхідний список data на пакети розміром batch_size і обчислює максимум для кожного пакету. Повертає список максимальних значень для кожного пакету.

Функція encode_string

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
Опис:
Ця функція кодує рядок string згідно з алгоритмом подвійної кодування, де кожен символ після кількості повторень записується в кінці. Наприклад, рядок "aaabbcc" буде закодовано як "3a2b2c".

Функція decode_string

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
Опис:
Ця функція декодує закодований рядок encoded, замінюючи кожен символ, що повторюється, відповідно до числа повторень. Наприклад, рядок "3a2b2c" буде декодовано як "aaabbcc".

Функція rotate_matrix

def rotate_matrix(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = matrix[i][j]

    return rotated
Опис:
Ця функція обертає квадратну матрицю matrix на 90 градусів вправо. Використовується нова матриця rotated для зберігання результату обертання.

Функція regex_search

def regex_search(strings, pattern):
    return [string for string in strings if re.search(pattern, string)]
Опис:
Ця функція здійснює пошук усіх рядків у списку strings, які відповідають вказаному регулярному виразу pattern. Повертає список рядків, які відповідають критеріям.

Функція merge_sorted_arrays

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
Опис:
Ця функція злиття двох відсортованих масивів arr1 і arr2 в один відсортований масив merged. Використовується алгоритм злиття двох відсортованих списків.

Функція is_prime

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
Опис:
Ця функція перевіряє, чи є число num простим. Використовується перевірка ділення на всі числа від 2 до квадратного кореня з num.

Функція group_by_key

def group_by_key(data, key):
    grouped = {}
    for item in data:
        if item[key] not in grouped:
            grouped[item[key]] = []
        grouped[item[key]].append(item['value'])
    return grouped
Опис:
Ця функція групує вхідний список словників data за значенням key. Кожному унікальному значенню key відповідає список значень з ключа 'value'.

Функція remove_outliers

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
Опис:
Ця функція видаляє викиди зі списку lst, використовуючи статистичні значення середнього значення та








