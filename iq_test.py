def iq_test(numbers):
    numbers_i = list(map(int, numbers.split()))
    answers_1 = [int(i) for i in numbers.split() if int(i) % 2 == 0]
    answers_2 = [int(i) for i in numbers.split() if int(i) % 2 != 0]
    if len(answers_1) == 1:
        return numbers_i.index(answers_1[0]) + 1
    else:
        return numbers_i.index(answers_2[0]) + 1


print(iq_test("1 2 1 1"))
