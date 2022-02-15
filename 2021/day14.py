#!/usr/local/bin/python3
input="""PFVKOBSHPSPOOOCOOHBP

FV -> C
CP -> K
FS -> K
VF -> N
HN -> F
FF -> N
SS -> K
VS -> V
BV -> F
HC -> K
BP -> F
OV -> N
BF -> V
VH -> V
PF -> N
FC -> S
CS -> B
FK -> N
VK -> H
FN -> P
SH -> V
CV -> K
HP -> K
HO -> C
NO -> V
CK -> C
VB -> S
OC -> N
NS -> C
NF -> H
SF -> N
NK -> S
NP -> P
OO -> S
NH -> C
BC -> H
KS -> H
PV -> O
KO -> K
OK -> H
OH -> H
BH -> F
NB -> B
FH -> N
HV -> F
BN -> S
ON -> V
CB -> V
CF -> H
FB -> S
KF -> S
PS -> P
OB -> C
NN -> K
KV -> C
BK -> H
SN -> S
NC -> H
PK -> B
PC -> H
KN -> S
VO -> V
FO -> K
CH -> B
PH -> N
SO -> C
KH -> S
HB -> V
HH -> B
BB -> H
SC -> V
HS -> K
SP -> V
KB -> N
VN -> H
HK -> H
KP -> K
OP -> F
CO -> B
VP -> H
OS -> N
OF -> H
KK -> N
CC -> K
BS -> C
VV -> O
CN -> H
PB -> P
BO -> N
SB -> H
FP -> F
SK -> F
PO -> S
KC -> H
VC -> H
NV -> N
HF -> B
PN -> F
SV -> K
PP -> K"""

test="""NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

both = input.split("\n\n")
template = both[0]
rules = dict([x.split(" -> ") for x in both[1].split("\n")])

pairs = {}
for i,c in enumerate(template[:-1]):
    pairs[c+template[i+1]] = pairs.get(c+template[i+1], 0) + 1
elements = {}
for c in template:
    elements[c] = elements.get(c, 0) + 1

for step in range(40):
    print(step)
    pairUpdate = {}
    for pair, count in pairs.items():
        if pair in rules:
            rule = rules[pair]
            elements[rule] = elements.get(rule, 0) + count
            newPairs = [pair[0] + rule, rule + pair[1]]
            for newPair in newPairs:
                pairUpdate[newPair] = pairUpdate.get(newPair, 0) + count
            pairUpdate[pair] = pairUpdate.get(pair, 0) - count

    for newPair, count in pairUpdate.items():
        pairs[newPair] = pairs.get(newPair, 0) + count

print(elements)
least = min(elements.values())
most = max(elements.values())
print(most - least)
