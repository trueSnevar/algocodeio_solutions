"""
Цепочка уникальных генов

средне
решено

Дана строка gene, представляющая последовательность генов, где каждый ген — это одна буква английского алфавита.

Требуется найти самую длинную непрерывную подстроку, в которой все гены уникальны (без повторяющихся букв).

Пример 1:

Ввод: gene = "yxyabcxyx"
Вывод: 5
Объяснение: "xyabc" или "yabcx" или "abcxy" самые длинные подстроки с длинной 5.

Пример 2:

Ввод: gene = "Aac"
Вывод: 3

Пример 3:

Ввод: gene = "ffff"
Вывод: 1

Ограничения:

0 <= len(gene)
Строка gene может быть содержать только английские буквы
"""

from typing import *

def longest_gene_sequence(gene: str) -> int:
    l = 0
    r = -1
    state = set()
    best = 0

    while l < len(gene):
        while r + 1 < len(gene) and gene[r + 1] not in state:
            state.add(gene[r + 1])
            r += 1

        best = max(best, r - l + 1)
        state.discard(gene[l])
        l += 1

    return best

if __name__ == "__main__":
    ex1 = "yxyabcxyx"

    ex2 = "Aac"

    ex3 = "ffff"

    ans1 = longest_gene_sequence(ex1)
    ans2 = longest_gene_sequence(ex2)
    ans3 = longest_gene_sequence(ex3)
    print(ans1)
    print(ans2)
    print(ans3)

"""
Оценка сложности

Время: O(n), где n - длина строки gene
Память: O(min(n, k)), где k - макс.размер словаря, а n - длина строки gene
"""