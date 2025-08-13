def front_back(str):
    if len(str) < 1:
        return str
    mid = str [len(str) - 1]
    return mid + str[1:len(str) -[1]] + str[0   ] 