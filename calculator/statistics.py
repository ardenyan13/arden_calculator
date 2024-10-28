def mean(data):
    if len(data) < 0:
        raise ZeroDivisionError("Can not divide by 0")
    return sum(data) / len(data)

def median(data):
    sorted_data = sorted(data)
    mid = len(data) // 2
    if len(data) % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid + 1]) / 2
    return sorted_data[mid]

def mode(data):
    from collections import defaultdict
    data_dict = defaultdict(int)
    for n in data:
        data_dict[n] += 1
    mode = None
    max_count = 0
    for key, count in data_dict.items():
        if count > max_count:
            max_count = count
            mode = key
    return mode

def standard_deviation(data):
    avg = mean(data)
    squared_differences = [(n - avg) ** 2 for n in data]
    variance = mean(squared_differences)
    return variance ** 0.5