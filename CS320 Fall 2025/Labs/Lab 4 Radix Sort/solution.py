import math


def radix_base(values_to_sort, base):
    if values_to_sort is None:
        raise ValueError("invalid arguments")
    if values_to_sort == []:
        raise ValueError("invalid arguments")
    if base < 2:
        raise ValueError("invalid arguments")
    
    try:
        for val in values_to_sort:
            if not isinstance(val, int) or val < 0:
                raise ValueError("invalid list element")
    except Exception:
        raise ValueError("invalid list element")
    
    if len(values_to_sort) < 2:
        return values_to_sort.copy()
    
    maxval = max(values_to_sort)
    x = 1
    output = values_to_sort.copy()
    while maxval // x > 0:
        parts = [[] for _ in range(base)]
        for num in output:
            digit = (num // x) % base
            parts[digit].append(num)
        output = []
        for part in parts:
            output.extend(part)
        x *= base
    return output
