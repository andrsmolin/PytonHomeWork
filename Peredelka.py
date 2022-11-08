# Апгрейд задания 5

# def create_list(lst):
#     list_cort = ["+"]
#     list_mix = []
#     for i in range(len(lst)):
#         if lst[i].count('*') > 0:
#             y = lst[i].find('x')
#             list_cort.append(lst[i][0:y-1])
#             list_cort.append(lst[i][y:])
#         else:
#             list_cort.append(lst[i])
#     print(list_cort)
#     while i != '=':
#         # for i in range(len(list_cort)):
#         if list_cort[i] == ("+" or list_cort[i] == "-") and list_cort[i+2].count('x') > 0:
#             list_mix[i] = (list_cort[i], list_cort[i+1], list_cort[i+2])
#             i += 3
#         elif list_cort[i] == ("+" or list_cort[i] == "-") and list_cort[i+2].count('x') == 0:
#             list_mix[i] = (list_cort[i], list_cort[i+1])
#             i += 2
#         # else:
#         #     a ==
#     print(list_mix)
#     return list_mix


# def max_list(l1, l2):
#     if len(l1) > len(l2):
#         return l1
#     else:
#         return l2


# def min_list(l1, l2):
#     if len(l1) < len(l2):
#         return l1
#     else:
#         return l2


def strip(m_list):
    m_list = list(map((lambda e: e.strip()), m_list))
    return m_list


def dict(list_b, list_z):
    list_b = [list_z[i] + list_b[i] for i in range(0, len(list_b))]
    list_col = [list_b[i].split('*') for i in range(0, len(list_b))]
    dic = {}
    for i in range(0, len(list_b)):
        dic[i] = (list_col[i][0], list_col[i][(len(list_col[i])-1)])
    # print(list_col)
    return dic


def work5():
    data = open('file_2x.txt', 'w')
    data1 = open('file.txt', 'r')
    data2 = open('file1.txt', 'r')
    f1 = data1.read()
    f2 = data2.read()
    list1 = f1.split("+" or "-")
    list2 = f2.split("+" or "-")
    list1[len(list1)-1] = list1[len(list1)-1][:-3]
    list2[len(list2)-1] = list2[len(list2)-1][:-3]
    list1 = strip(list1)
    list2 = strip(list2)
    list_z1 = [el for el in f1 if el == "+" or el == "-"]
    list_z2 = [el for el in f2 if el == "+" or el == "-"]
    list_z1.insert(0, '+')
    list_z2.insert(0, '+')
    dict_1 = dict(list1, list_z1)
    dict_2 = dict(list2, list_z2)
    len_max = max(len(dict_1), len(dict_2))
    for i in range(0, len_max):

        # max_l = max_list(list1, list2)
        # min_l = min_list(list1, list2)
        # for i in list1:
        #     for a in list2:
        # if list1[i].count("**5") > 0 and list2[a].count("**5"):

    # print(f1)
    # print(f2)
    # print(list_z1)
    # print(list1)
    # print(list2)
    # print(dict_1)
    # print(dict_2)
    # print(dict_1)

    # list_cort1 = create_list(list1)
    # list_cort2 = create_list(list2)
    # list_big = []
    # for i in range(max(len(list1), len(list2))):
    #     if list_cort1[i].count('*') > 0:
    #         for y in range(0, len(list1[i])):
    #             # x_index = list1[i].find('x')
    #             if list1[i][y] == "x":
    #                 list_cort1.append(list1[i][0:y-1])
    #                 list_cort1.append(list1[i][y:])
    #     else:
    #         list_cort1.append(list1[i])
    # print(list_cort1)
    # list2.insert(0, "+")
    # list1.remove("=")
    # list1.remove("0")
    # for i in range(0, len(list1)):
    #     data.write(f"{list1[i]} ")
    # for i in range(0, len(list2)):
    #     data.write(f"{list2[i]} ")
    # data.close
    # data1.close
    # data2.close


# work5()