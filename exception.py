def first_fanc():
    n = int(input())
    args = {}
    for i in range(n):
        x = input()
        if ' ' not in x:
            args[x] = ''
        elif ' ' in x:
            a = x.split()
            args[a[0]] = set(a[2:])
    return args


def exceptions(dict_main, exception_, result_list, value_list):
    if dict_main[exception_] == '':
        return
    for value_tuple_dict in dict_main[exception_]:
        if value_tuple_dict == value_list:
            return True
        elif exceptions(dict_main, value_tuple_dict, result_list, value_list):
            return True
        elif dict_main[value_tuple_dict] == '':
            continue


def enumeration(main_list, result_list, dict_main, number_of_exceptions):
    for i in range(number_of_exceptions):
        exception_ = input()
        if len(main_list) == 0:
            main_list.append(exception_)
            continue
        for value_list in main_list:
            if exceptions(dict_main, exception_, result_list, value_list):
                if exception_ not in result_list:
                    result_list.append(exception_)
        main_list.append(exception_)
    return main_list, result_list


def second_fanc(dict_main):
    number_of_exceptions = int(input())
    main_list = []
    result_list = []
    enumeration(main_list, result_list, dict_main, number_of_exceptions)
    print(*result_list)


second_fanc(first_fanc())
