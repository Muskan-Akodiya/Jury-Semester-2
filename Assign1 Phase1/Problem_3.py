"""
Problem 3: Reflection or Pratibimb 

Design and Develop a User Defined function named (reflection) pass the input literal 'Welcome to EN2004' and return Output Format Mentioned Below

Input Format:

1. Take M str input from the User 
2. Get M , seperated str literals from a user (Test string to pass: 'Welcome to EN2004')

Output Format:

EN2004
to
Welcome



"""
n=int(input())
M =str(input())
def reflection(M):
    words=M.split(',')
    reversed_words=words[::-1]
    reverse_sentence='\n'.join(reversed_words)
    return reverse_sentence

print(reflection(M))
