"""
Цепочка из k-генов

средне
решено

Дана строка gene, представляющая последовательность генов, где каждый ген — это один символ.

Требуется найти самую длинную непрерывную подстроку, содержащую не более k уникальных генов,
где k ≤ числа различных символов.

Пример 1:

Ввод: gene = "YYxxXXXyyy", k = 3
Вывод: 8
Объяснение: самая длинная непрерывная последовательность генов с максимум 3-мя разными генами
это "xxXXXyyy" (регистр буквы имеет значение).

Пример 2:

Ввод: gene = "yyy", k = 0
Вывод: 0

Пример 3:

Ввод: gene = "aXYYYXYXYbccc", k = 1
Вывод: 3

Ограничения:

0 <= len(gene)
0 <= k <= len(gene)

"""

from typing import *
from collections import defaultdict


def longest_gene_sequence(gene: str, k: int) -> int:
    # l = 0
    # state = defaultdict(int)
    # best = 0
    #
    # for r in range(len(gene)):
    #     state[gene[r]] += 1
    #     while len(state) > k:
    #         state[gene[l]] -= 1
    #         if state[gene[l]] == 0:
    #             del state[gene[l]]
    #         l += 1
    #     best = max(best, r - l + 1)
    #
    # return best

    l = 0
    # r = -1, чтобы добавление первого элемента не было исключением
    r = -1
    result = 0
    geneCount = defaultdict(int)

    while l < len(gene):
        while r + 1 < len(gene) and (len(geneCount) < k or gene[r + 1] in geneCount):
            geneCount[gene[r + 1]] += 1
            r += 1

        # обновляем ответ
        windowSize = r - l + 1
        result = max(result, windowSize)

        # двигаем l (левую границу окна) на 1 и обновляем число уникальных символов
        geneCount[gene[l]] -= 1
        if geneCount[gene[l]] <= 0:
            # <=, а не == т.к. при k = 0 geneCount[gene[l]] -= 1 добавит ключ gene[l]
            # а так происходить не должно, поэтому условие <= 0
            # Чтобы лучше понять можешь посмотреть что происходит при gene="xyz" k = 0
            del geneCount[gene[l]]
        l += 1
    return result

if __name__ == "__main__":
    ex1 = "YYxxXXXyyy"
    k1 = 3

    ex2 = "yyy"
    k2 = 0

    ex3 = "aXYYYXYXYbccc"
    k3 = 1

    ans1 = longest_gene_sequence(ex1, k1)
    ans2 = longest_gene_sequence(ex2, k2)
    ans3 = longest_gene_sequence(ex3, k3)
    print(ans1)
    print(ans2)
    print(ans3)

"""
Оценка сложности

Время: O(n), где n - длина строки gene
Память: O(min(n, k)), где k - макс.размер словаря, а n - длина строки gene
"""