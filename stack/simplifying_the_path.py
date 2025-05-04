"""
Упрощение пути

средне
решено

Дан абсолютный путь path в файловой системе Unix. Нужно вернуть его упрощенный канонический вид.

Правила преобразования:

. — текущий каталог (игнорируется).
.. — переход на уровень выше (удаляет предыдущий каталог).
Несколько / подряд заменяются на один.
Путь должен начинаться с / и не заканчиваться им (кроме корня).

Пример 1:

Ввод: path = "/usr/local/"
Вывод: "/usr/local"
Объяснение: Лишняя косая черта в конце удалена.

Пример 2:

Ввод: path = "/var//www/html/"
Вывод: "/var/www/html"
Объяснение: Лишние косые черты заменены на одну.

Пример 3:

Ввод: path = "/tmp/.../a/../b/c/../d/./"
Вывод: "/tmp/.../b/d"

Ограничения:

len(path) >= 1
path всегда начинается с /.
"""

from typing import *

def simplify_path(path: str) -> str:
    stack = []
    for name in path.split("/"):
        if name == "." or name == "":
            continue
        elif name == "..":
            if stack:
                stack.pop()
        else:
            stack.append(name)
    return "/" + "/".join(stack)

if __name__ == "__main__":
    ex1 = "/usr/local/"
    ex2 = "/var//www/html/"
    ex3 = "/tmp/.../a/../b/c/../d/./"

    ans1 = simplify_path(ex1)
    ans2 = simplify_path(ex2)
    ans3 = simplify_path(ex3)

    print(ans1)
    print(ans2)
    print(ans3)



"""
Оценка сложности

Время: O(n), где n - длинна строки path
Память: O(n), где n - длинна строки path
"""

