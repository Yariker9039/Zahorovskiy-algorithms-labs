"""Лабораторна 8. Швидкий пошук ключів. Python 3.8+."""
from dataclasses import dataclass


@dataclass
class Client:
    id: int
    name: str


@dataclass
class Order:
    number: int
    clientId: int
    sum: int


clients = [Client(101, 'Коваленко'), Client(102, 'Мельник'),
           Client(103, 'Шевчук'), Client(104, 'Бондар'),
           Client(105, 'Ткачук'), Client(106, 'Гриценко')]
orders = [Order(1, 103, 450), Order(2, 101, 120),
          Order(3, 105, 980), Order(4, 103, 300),
          Order(5, 102, 75), Order(6, 106, 1500),
          Order(7, 101, 220), Order(8, 103, 60)]
blocked = [102, 104]


# Старий фрагмент 1:
# for order in orders:
#     for client in clients:
#         if client.id == order.clientId:
#             print(f'Замовлення {order.number} — {client.name}')
def fragment1():
    byId = {client.id: client for client in clients}
    for order in orders:
        print(f'Замовлення {order.number} — {byId[order.clientId].name}')


# Старий фрагмент 2:
# total = 0
# for order in orders:
#     if order.clientId not in blocked:
#         total += order.sum
# print(f'Сума прийнятих замовлень: {total}')
def fragment2():
    blockedIds = set(blocked)
    total = 0
    for order in orders:
        if order.clientId not in blockedIds:
            total += order.sum
    print(f'Сума прийнятих замовлень: {total}')


# Старий фрагмент 3:
# counted = []
# for order in orders:
#     if order.clientId in counted:
#         continue
#     count = 0
#     for other in orders:
#         if other.clientId == order.clientId:
#             count += 1
#     counted.append(order.clientId)
#     print(f'{order.clientId}: {count}')
def fragment3():
    counts = {}
    for order in orders:
        counts[order.clientId] = counts.get(order.clientId, 0) + 1
    # Порядок задає вихідний список, а множина лише пам'ятає надруковані id.
    printed = set()
    for order in orders:
        if order.clientId not in printed:
            print(f'{order.clientId}: {counts[order.clientId]}')
            printed.add(order.clientId)


# Фрагмент 4 залишено без зміни алгоритму: достатньо одного проходу.
def fragment4():
    best = orders[0]
    for order in orders:
        if order.sum > best.sum:
            best = order
    print(f'Найбільше замовлення: {best.sum}')


# Фрагмент 5 залишено за умовою. Нова структура не потрібна.
# Помилка ефективності: byId будується всередині циклу 8 разів.
# Достатньо винести його створення перед циклом, як у fragment1.
def fragment5():
    for order in orders:
        byId = {}
        for client in clients:
            byId[client.id] = client
        print(f'Замовлення {order.number} — {byId[order.clientId].name}')


def main():
    for number, fragment in enumerate([fragment1, fragment2, fragment3, fragment4, fragment5], 1):
        print(f'Фрагмент {number}')
        fragment()


if __name__ == '__main__':
    main()
