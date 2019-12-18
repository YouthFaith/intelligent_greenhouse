# -*- coding: utf-8 -*-

def get_res(test):
    res = 0
    while 1:
        res += test // 3
        test = test // 3 + test % 3
        if test == 1:
            print(res)
            break
        elif test == 2:
            print(res + 1)
            break

if __name__ == "__main__":
    while 1:
        test = input()
        if int(test) == 0:
            break
        else:
            get_res(int(test))
    # print(3 // 1)