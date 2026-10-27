"""Перевірка результатів: python check_labs.py."""
import contextlib
import importlib.util
import io
import pathlib
import sys


def load(n):
    spec = importlib.util.spec_from_file_location(f'lab{n}', pathlib.Path(__file__).parent / f'lab{n:02}' / 'main.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def capture(fn, *args):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        result = fn(*args)
    return result, out.getvalue()


s = load(4)
expected_counts = [(1, 7), (15, 7), (8, 1), (15, 8), (15, 8), (15, 8), (1, 1), (0, 0)]
cases = [(s.sortedData, x, idx) for x, idx in [(3, 0), (71, 14), (31, 7), (1, -1), (99, -1), (50, -1)]]
cases += [([42], 42, 0), ([], 42, -1)]
for (items, target, expected), counts in zip(cases, expected_counts):
    for fn, count in zip([s.linearSearch, s.binarySearch], counts):
        s.comparisons = 0
        assert fn(items, target) == expected
        assert s.comparisons == count
for size in range(30):
    items = list(range(0, size * 2, 2))
    for target in range(-1, size * 2 + 2):
        expected = items.index(target) if target in items else -1
        assert s.linearSearch(items, target) == expected
        assert s.binarySearch(items, target) == expected
assert s.binarySearch(s.data, 55) == -1
print('lab04: 8 випадків, лічильники та додаткові межові перевірки — OK')
s = load(5)
names = lambda items: [x.surname for x in items]
assert names(sorted(s.students, key=s.surnameKey)) == ['Бондар','Гриценко','Дяченко','Іваненко','Коваль','Мельник','Сидоренко','Ткаченко']
by_grade = sorted(s.students, key=lambda x: -x.grade)
assert names([x for x in by_grade if x.grade == 85]) == ['Ткаченко','Іваненко','Сидоренко','Дяченко']
assert names(sorted(s.students, key=lambda x: (-x.grade, s.surnameKey(x)))) == ['Бондар','Мельник','Дяченко','Іваненко','Сидоренко','Ткаченко','Гриценко','Коваль']
assert names(sorted(s.students, key=lambda x: (x.group, -x.grade))) == ['Ткаченко','Іваненко','Сидоренко','Гриценко','Бондар','Мельник','Дяченко','Коваль']
assert capture(s.main)[1] == capture(s.main)[1]
print('lab05: українська абетка, стабільність, складені ключі, повторний запуск — OK')
s = load(6)
s.callCount = 0
assert s.countProducts(s.catalog) == 93 and s.callCount == 12
s.callCount = 0
assert s.maxDepth(s.catalog) == 4 and s.callCount == 12
s.callCount = 0
assert len(capture(s.printTree, s.catalog, 0)[1].splitlines()) == 12 and s.callCount == 12
leaf = s.Category('Листок', 8, [])
assert s.maxDepth(leaf) == 1 and s.countProducts(leaf) == 8
print('lab06: дерево, товари, глибина, виклики, листок — OK')
s = load(7)
assert [s.isBalanced(x) for x in s.lines] == [True,True,True,False,False,False,True]
total, output = capture(s.processQueue, s.requests)
assert total == 31 and 'Перескладання з 19 до 28 хв' in output and '12.50' in output
assert capture(s.processQueue, [])[0] == 0
print('lab07: всі рядки, FIFO, очікування, порожня черга — OK')
s = load(8)
# Виконуємо саме старі закоментовані блоки, щоб порівняти повний вивід.
source = pathlib.Path(s.__file__).read_text(encoding='utf-8')
for number in [1, 2, 3]:
    block = source.split(f'# Старий фрагмент {number}:\n')[1].split(f'def fragment{number}():')[0]
    old_code = '\n'.join(line[2:] for line in block.splitlines() if line.startswith('# '))
    old_output = capture(exec, old_code, vars(s).copy())[1]
    new_output = capture(getattr(s, f'fragment{number}'))[1]
    assert old_output == new_output
assert capture(s.fragment1)[1] == capture(s.fragment5)[1]
assert '3630' in capture(s.fragment2)[1]
assert capture(s.fragment3)[1] == '103: 3\n101: 2\n105: 1\n102: 1\n106: 1\n'
assert '1500' in capture(s.fragment4)[1]
assert len({c.id for c in s.clients} - {o.clientId for o in s.orders}) == 1
print('lab08: старий і новий вивід збігаються повністю, усі підсумки — OK')
