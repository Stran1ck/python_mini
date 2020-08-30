"""Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

﻿Пример выходного файла:
ff
dde
c
ab

"""
a = []
with open("dataset_24465_4.txt", "r") as inp, open("dataset_24465_4_1.txt", "w") as out:
    for line in inp:
        a.append(line)
    a.reverse()
    for line in a:
        out.write(line)
