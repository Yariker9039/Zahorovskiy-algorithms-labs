"""Лабораторна 7. Готові стек і черга з collections."""
from collections import deque
from dataclasses import dataclass

lines = ['', 'a + b', '{[a] + (b)}', '([)]', 'a)', '(a[b]', 'f(x[1]) * {y + (z)}']


@dataclass
class Request:
    name: str
    minutes: int


requests = [
    Request('Довідка про навчання', 4),
    Request('Академічна відпустка', 7),
    Request('Копія наказу', 2),
    Request('Виписка з оцінками', 6),
    Request('Перескладання', 9),
    Request('Студентський квиток', 3),
]


def isBalanced(line):
    stack = deque()
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in line:
        if char in '([{':
            stack.append(char)
        elif char in pairs:
            if not stack:
                return False
            if stack.pop() != pairs[char]:
                return False
    return not stack


def processQueue(requests):
    queue = deque(requests)
    if not queue:
        print('Обробляти нічого. Оброблено заявок: 0, загальний час: 0 хв')
        return 0
    elapsed = 0
    waiting = 0
    count = 0
    while queue:
        request = queue.popleft()
        count += 1
        waiting += elapsed
        print(f'{count}. {request.name} з {elapsed} до {elapsed + request.minutes} хв')
        elapsed += request.minutes
    print(f'Оброблено заявок: {count}, загальний час: {elapsed} хв')
    print(f'Середній час очікування: {waiting / count:.2f} хв')
    return elapsed


def main():
    for line in lines:
        print(f"{line or '(порожній рядок)'} -> {'так' if isBalanced(line) else 'ні'}")
    print('Збалансованих:', sum(isBalanced(line) for line in lines))
    processQueue(requests)
    print('Перевірка порожньої черги:')
    processQueue([])


if __name__ == '__main__':
    main()
