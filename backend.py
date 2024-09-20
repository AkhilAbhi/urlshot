


def pointcount(point):
    point = int(point)
    re = 2
    if(point < 5):
        re = 2
    elif (point < 10 and point > 4):
        re = 3
    elif (point < 15 and point > 9):
        re = 4
    else:
        re = 5
    return re