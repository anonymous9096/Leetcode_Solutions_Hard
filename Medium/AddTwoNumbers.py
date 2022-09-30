def ATN(l1, l2):
    l1.reverse()
    l2.reverse()
    x = int(''.join(map(str, l1)))
    y = int(''.join(map(str, l2)))
    sum = x + y
    BeReverseList = list(str(sum))
    BeReverseList.reverse()
    print(BeReverseList)

if __name__=="__main__":
    l1, l2 = [2,4,3], [5,6,4]
    ATN(l1, l2)
