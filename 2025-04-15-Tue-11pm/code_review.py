#!/usr/bin/python3

#input A : patchset 1
A = [[1,4,'comment1'],[2,2,'comment2'],[4,8,'comment3'],[12,15,'comment4']]
#input B : patchset 2
B = [[2,3],[9,9],[15,15]]

#res = [[1,4],[2,2],[12,15]]

'''
# solv 1
res = []

# fine the max file line
FILE_LINE = 20
modified_line = [0] * FILE_LINE

for s, e in B:
    modified_line[s] += 1
    modified_line[e + 1] -= 1

for i in range(1, len(modified_line)):
    modified_line[i] += modified_line[i - 1]

for s, e, cmt in A:
    for i in range(s, e + 1):
        if modified_line[i] != 0:
            res.append([s,e])
            break

print(res)
'''
# solv 2
res = []
bit_mask = 0

# Set modified line to bit
for s, e in B:
    bit_cnt = e + 1 - s
    bit_mask |= ((2 ** bit_cnt - 1) << s)

# Check if the commented area has been modified
for s, e, cmt in A:
    bit_cnt = e + 1 - s
    if ((2 ** bit_cnt - 1) << s) & bit_mask:
        res.append([s,e])

print(res)
