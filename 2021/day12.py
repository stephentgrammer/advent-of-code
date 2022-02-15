#!/usr/local/bin/python3

input = """lg-GW
pt-start
pt-uq
nx-lg
ve-GW
start-nx
GW-start
GW-nx
pt-SM
sx-GW
lg-end
nx-SM
lg-SM
pt-nx
end-ve
ve-SM
TG-uq
end-SM
SM-uq"""

test1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

test2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

test3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

import itertools as it

def listFind(haystack, needles):
    l = len(needles)
    for i in range(len(haystack)):
        if haystack[i:i+l] == needles:
            return True

def pathfind(paths, byCave, path = ["start"]):
    # print(path, byCave[path[-1]])
    for step in byCave[path[-1]]:
        if step == "start":
            pass
        elif step == "end":
            paths.append(path + [step])
        # elif step[0].islower(): # puzzle 1
            # if step not in path:
                # pathfind(paths, byCave, path + [step])
        elif step.islower(): # puzzle 2
            lowers = [x for x in path if x.islower()]
            if step not in path or len(set(lowers)) == len(lowers):
                pathfind(paths, byCave, path + [step])
        else:
            pathfind(paths, byCave, path + [step])

def solve(string):
    connexions = [x.split("-") for x in string.split("\n")]
    connexions += [[x[1], x[0]] for x in connexions]
    caves = set(it.chain.from_iterable(connexions))
    byCave = dict([(x, [y[1] for y in connexions if y[0] == x]) for x in caves])

    paths = []
    pathfind(paths, byCave)
    # for path in paths:
        # print(",".join(path))
    solution = len(set([str(x) for x in paths]))
    print(solution)
    return solution

# puzzle 1
# assert solve(test1) == 10, "test 1 failed"
# assert solve(test2) == 19, "test 2 failed"
# assert solve(test3) == 226, "test 3 failed"
# puzzle 2
assert solve(test1) == 36, "test 1 failed"
assert solve(test2) == 103, "test 2 failed"
assert solve(test3) == 3509, "test 3 failed"
solve(input)
