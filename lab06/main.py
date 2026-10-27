"""Лабораторна 6. Рекурсивний обхід."""
from dataclasses import dataclass


@dataclass
class Category:
    name: str
    products: int
    children: list


catalog = Category('Каталог', 0, [
    Category('Одяг', 0, [
        Category('Верхній одяг', 0, [
            Category('Куртки', 12, []), Category('Пальта', 7, []),
        ]),
        Category('Светри', 15, []),
    ]),
    Category('Взуття', 4, [
        Category('Кросівки', 23, []), Category('Чоботи', 9, []),
    ]),
    Category('Аксесуари', 0, [
        Category('Сумки', 18, []), Category('Ремені', 5, []),
    ]),
])
callCount = 0


def printTree(node, level):
    global callCount
    callCount += 1
    print('  ' * level + node.name)
    for child in node.children:
        printTree(child, level + 1)


def countProducts(node):
    global callCount
    callCount += 1
    if not node.children:
        return node.products
    total = node.products
    for child in node.children:
        total += countProducts(child)
    return total


def maxDepth(node):
    global callCount
    callCount += 1
    if not node.children:
        return 1
    return 1 + max(maxDepth(child) for child in node.children)


def main():
    global callCount
    callCount = 0
    printTree(catalog, 0)
    print('Рядків дерева:', callCount)
    callCount = 0
    print('Товарів:', countProducts(catalog))
    print('Викликів countProducts:', callCount)
    callCount = 0
    print('Глибина:', maxDepth(catalog))
    print('Викликів maxDepth:', callCount)


if __name__ == '__main__':
    main()
