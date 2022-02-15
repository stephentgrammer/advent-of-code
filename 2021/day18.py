#!/usr/local/bin/python3

def add(a, b):
    return [a, b]

assert add([[[[4,3],4],4],[7,[[8,4],9]]], [1,1]) == [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]

left = []
right = []
def explode(a, side = "both"):
    global left, right
    print(a, " => ", left, "=>", right)
    if side == "both":
        left = []
        right = []
    if isinstance(a, list):
        if len(left) == 4 or len(right) == 4:
            aa = left[-1]
            while isinstance(aa, list) and len(left) > 1:
                left.pop()
                aa = left[-1]
            if isinstance(aa, list):
                a[0] = 0
            else:
                left[-1] += a[0]
            bb = right[-1]
            while isinstance(bb, list) and len(right) > 1:
                right.pop()
                bb = right[-1]
            if isinstance(bb, list):
                a[1] = 0
            else:
                right[-1] += a[1]

            return 0
        else:
            left.append(a[0])
            right.append(a[1])

        tempa = None
        tempb = None
        if isinstance(a[0], list):
            tempa = explode(a[0], "left")
            tempb = explode(a[1], "right")
        else:
            tempb = explode(a[1], "right")
            tempa = explode(a[0], "left")

        return [tempa, tempb]
    else:
        if side == "left":
            return left.pop()
        elif side == "right":
            return right.pop()
        else:
            return a



# assert explode([[[[0,9],2],3],4]) == [[[[0,9],2],3],4]
# assert explode([[[[[9,8],1],2],3],4]) == [[[[0,9],2],3],4]
# assert explode([7,[6,[5,[4,[3,2]]]]]) == [7,[6,[5,[7,0]]]]
# assert explode([[6,[5,[4,[3,2]]]],1]) == [[6,[5,[7,0]]],3]
# assert explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]) == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
print(explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]))
assert explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]) == [[3,[2,[8,0]]],[9,[5,[7,0]]]]

# def split(b):
    # return a

# def reduce(a):

    # changed, a = explode(a)
    # if changed:
        # return reduce(a)

    # changed, a = explode(a)
    # if changed:
        # return reduce(a)

    # return a

# assert reduce([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]) == [[[[0,7],4],[[7,8],[6,0]]],[8,1]]

def magnitude(a):
    if not isinstance(a, list):
        return a
    return 3 * magnitude(a[0]) + 2 * magnitude(a[1])

assert magnitude([[1,2],[[3,4],5]]) == 143
assert magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]]) == 1384
assert magnitude([[[[1,1],[2,2]],[3,3]],[4,4]]) == 445
assert magnitude([[[[3,0],[5,3]],[4,4]],[5,5]]) == 791
assert magnitude([[[[5,0],[7,4]],[5,5]],[6,6]]) == 1137
assert magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]) == 3488

