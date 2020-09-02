# def get_len_of_str(string):
#     new_string = set(string)
#     str_len = len(new_string)
#     return str_len

# x = 'abcddddjklmnopddf'
# m = list(x)
# print(m[1])
# # # print(m)
# k = len(m)
# new_lst = []
# for i in range(0, k):
#     for n in range(i+1, k+1):
#         if m[i] == m[n]:
        # if m[i] == m[n]:
            # new_lst.append(m[0:i])

    # print(x[i])
    # for n in range(i+1, len(x)):
    #     print(x[n])
    #     if x[i] == x[n]:
    #         print(x[0:i])
    #         # new_lst.append(x[0:i])
    #         # print(new_lst)

# x = ['abcddddjklmnopddf']
# new_lst = []
# for i in str(x):
#     if i.count(str(x)) == 1:
#         new_lst.append(i)
#     if i.count(str(x)) > 1: 
#         new_lst.append(i)

# print(new_lst)



def get_len_of_str(string):
    new_list = []
    n = 0
    for i in string:
      if i in new_list:
          print(i)
          new_list = new_list[new_list.index(i) + 1:]

    new_list.append(i)
    n = max(n, len(new_list))
      
    return n

# print(get_len_of_str('abbbcdefg'))


#     # abcd
# abcddddjklmnopddf

    # jklmnopd

    # df

    # abcd djklmnop
    # pwooabco

    # pwo
    # oabc
    # o
    # p w o a b c 
    # abco