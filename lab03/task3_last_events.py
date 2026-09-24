# Задача 3. Останні N подій.
# Масив на N позицій + номер комірки, у яку писати далі.
# Найстаріша подія просто перезаписується, нічого не зсувається.

N = 5

events = [f"Подія {i}" for i in range(1, 9)]  # потік із 8 подій

buffer = [None] * N   # масив фіксованого розміру
next_cell = 0         # у яку комірку писати наступного разу
count = 0             # скільки подій усього надійшло

for event in events:
    buffer[next_cell] = event
    next_cell += 1
    if next_cell == N:  # дійшли до кінця масиву — починаємо з нуля
        next_cell = 0
    count += 1

# Виводимо від найстарішої до найновішої.
# Якщо подій менше за N — вони лежать з комірки 0.
# Інакше найстаріша лежить там, куди писати наступного разу (next_cell).
stored = min(count, N)
start = 0 if count < N else next_cell

for k in range(stored):
    print(buffer[(start + k) % N])
