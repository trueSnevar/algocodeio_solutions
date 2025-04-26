"""
Поиск мутирующего вируса

средне
решено

Необходимо вернуть true, если в строке gene встречается строка virus или любая другая строка,
которая является пермутацией строки virus.

Пермутацией строки называется любая перестановка ее букв.
Например, для строки "abb" пермутациями будут "bab" и "bba".

Пример 1:

Ввод: gene = "cdeebba", virus = "abb"
Вывод: true
Объяснение: нужно проверить есть ли в строке "cdeebba" подстрока "abb" или "bab" или "bba".
Есть подстрока "bba" поэтому вернем true

Пример 2:

Ввод: gene = "xyxxux", virus = "xxx"
Вывод: false

Пример 3:

Ввод: gene = "monstergen", virus = "ster"
Вывод: true

Ограничения:

0 <= len(gene)
0 <= len(virus)
Строка gene и строка virus могут содержать только английские буквы
"""

from typing import *
from collections import defaultdict

def check_for_virus(gene: str, virus: str) -> bool:
    pattern = defaultdict(int)

    for char in virus:
        pattern[char] += 1

    l = 0
    r = -1
    state = defaultdict(int)

    while l < len(gene):
        while r + 1 < len(gene) and len(state) < len(pattern):
            state[gene[r + 1]] += 1
            r += 1

        if state == pattern:
            return True

        state[gene[l]] -= 1
        if state[gene[l]] <= 0:
            del state[gene[l]]

        l += 1

    return False

if __name__ == "__main__":
    gene1 = "cdeebba"
    virus1 = "abb"

    gene2 = "xyxxux"
    virus2 = "xxx"

    gene3 = "monstergen"
    virus3 = "ster"


    ans1 = check_for_virus(gene1, virus1)
    ans2 = check_for_virus(gene2, virus2)
    ans3 = check_for_virus(gene3, virus3)
    print(ans1)
    print(ans2)
    print(ans3)

"""
Оценка сложности

Время: O(n), где n - длина gene
Память: O(1)
"""