""" 

Problem: Knock Knock are you there?

Input Format:

1. Take M int input from the User 
2. Get M , seperated values from a user 
3. Enter a number 'N' you are looking for

Output Format:

1. Print index on console once Found or Print 'Better Luck Next Time' to the console


"""
M=int(input())
values=list(map(int, input().split(',')))
N=int(input())

def find_index(values, N):
    for i in range(len(values)):
        if values[i]==N:
            return i
            return "Better Luck Next Time"
print(find_index(values, N))
