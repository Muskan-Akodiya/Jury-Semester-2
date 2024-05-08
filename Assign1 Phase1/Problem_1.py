"""
Given a list of length M, you need to print and find sum of the elements of list 

Input Format :

Line 1 : An int M 
Line 2 : M int elements of list seperated by ';'

Output Format:

Addition 

Constraints :
1 <= M <= 10^6

"""
M=int(input())
ilist = list(map(int, input().split(';')))
def find_sum(M, ilist):
    sum = 0
    for i in range(M):
        sum += ilist[i]
    print(sum)

find_sum(M, ilist)
