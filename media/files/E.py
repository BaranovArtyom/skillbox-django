def take_syms(dic, string):
    for sym in string:
        if sym in dic:
            dic[sym] += 1
        else:
            dic[sym] = 1


a = input()
b = input()

dic1 = dict()
dic2 = dict()

take_syms(dic1, a)
take_syms(dic2, b)

if len(dic1) != len(dic2):
    print(0)
else:
    for key in dic1.keys():
        if dic1.get(key) != dic2.get(key):
            print(0)
            break
    else:
        print(1)


