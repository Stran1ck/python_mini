"""
По случаю 100500-летия Берляндского государственного университета совсем скоро состоится бал!
Уже n юношей и m девушек во всю репетируют вальс, менуэт, полонез и кадриль.

Известно, что на бал будут приглашены несколько пар юноша-девушка, причем уровень умений танцевать партнеров
в каждой паре должен отличаться не более чем на единицу.

Для каждого юноши известен уровень его умения танцевать. Аналогично,
для каждой девушки известен уровень ее умения танцевать. Напишите программу,
которая определит наибольшее количество пар, которое можно образовать из n юношей и m девушек.

Входные данные

В первой строке записано целое число n (1 ≤ n ≤ 100) — количество юношей.
Вторая строка содержит последовательность a1, a2, ..., an (1 ≤ ai ≤ 100),
где ai — умение танцевать i-го юноши.

Аналогично, третья строка содержит целое m (1 ≤ m ≤ 100) – количество девушек.
В четвертой строке содержится последовательность b1, b2, ..., bm (1 ≤ bj ≤ 100),
где bj — умение танцевать j-й девушки.

Выходные данные

Выведите единственное число — искомое максимальное возможное количество пар.

Sample Input 1:

4
1 4 6 2
5
5 1 5 7 9
Sample Output 1:

3

"""


def ball(x, list_big, list_small):
    c = 0
    i = 0
    while i < x:
        c += list_big.count(list_small[i])
        i += 1
    return c


n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
if n < m:
    print(ball(n, m_list, n_list))
else:
    print(ball(m, n_list, m_list))
