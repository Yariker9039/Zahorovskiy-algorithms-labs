"""Лабораторна 4. Пошук у даних."""

data = [42, 8, 60, 19, 3, 55, 12, 31, 68, 24, 49, 37, 71, 5, 27]
sortedData = sorted(data.copy())
comparisons = 0


def linearSearch(items, target):
    global comparisons
    for i in range(len(items)):
        comparisons += 1
        if items[i] == target:
            return i
    return -1


def binarySearch(items, target):
    global comparisons
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if items[mid] == target:
            return mid
        comparisons += 1
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def report(name, items, target):
    global comparisons
    comparisons = 0
    index = linearSearch(items, target) if name == 'linear' else binarySearch(items, target)
    print(name, target, index, comparisons)


def main():
    print('Масив:', sortedData)
    print('Метод, значення, індекс, порівняння')
    cases = [(sortedData, x) for x in [3, 71, 31, 1, 99, 50]]
    cases += [([42], 42), ([], 42)]
    for items, target in cases:
        report('linear', items, target)
        report('binary', items, target)
    print('Невідсортований масив, шукаємо 55:')
    report('binary', data, 55)


if __name__ == '__main__':
    main()
