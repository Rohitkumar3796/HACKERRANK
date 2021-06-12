# '''LIST COMPREHENSION MEANS PRINT CHARACTER OR SOMETHING IN A LINE
#  and print number lexicographically
# ABC=ACB,BAC,BCA,CAB,CBA #First character should be sorted
# increasing order :1,2,3,4,5
# lexicographically or non-decreasing order :1,2,2,3,3,4,5 increasing + Equal before number or character
# '''
# if __name__ == '__main__':
#     x = int(input("num1"))
#     y = int(input("num2"))
#     z = int(input("num3"))
#     n = int(input("N"))
#     l=list()
#     for i in range(x+1):
#         for j in range(y+1):
#             for k in range(z+1):
#                 if (i+j+k!=n): #when i+j+k is not equal to n then print
#                     l.append([i,j,k])
#     print(l)
# =================================================================
# x,y,z,n=[int(input("enter the number")) for i in range(4)]
# print([[i,j,k] for i in range(x+1)  for j in range(y+1) for k in range(z+1)  if (x+y+z)!=n])
# ====================================================================
# 'RUNNER UP SCORE MAX IS 6 and RUNNER UP IS 5'
# if __name__ == '__main__':
#     n = int(input("how much"))
#     arr = list(map(int, input("enter element").split()))
#     arr.sort()
#     print(arr[(arr.index(max(arr)))-1])
# =================================================================
# SECOND HIGHEST(MAX) IN THE LIST
# if __name__ == '__main__':
#     n = int(input("enter"))
#     arr=list(map(int,input("enter the list of element").split())) #here we making a list by lap function  in one statement
#     maximum=max(arr)
#     # print(maximum)
#     c=arr.count(maximum)
#     # print(c)
#     for i in range(c): #here we use for loop to traverse repeated maximum element in list
#         arr.remove(maximum)
#     # print(arr)
#     print(max(arr))
# -----------------------------------------------------------------------
# SECOND LOWEST GRADE WITH THEIR NAME OD STUDENT AND PRINT ONLY THEIR NAMES
# if __name__ == '__main__':
#     name_score=[]
#     grade=[] #here is grade list for append grade value seprately
#     n=int(input("n"))
#     for i in range(n):
#         name=input("enter the name")
#         score=float(input("enter the score"))
#         name_score.append([name,score])
#         grade.append(score)
#     sort_grade=sorted(set(grade))
#     second_lowest=sort_grade[1]
#     stud_name = []
#     for val in name_score:
#         if second_lowest==val[1]:
#             stud_name.append(val[0])
#     stud_name.sort()
#     for j in stud_name:
#         print(j)
# -------------------------------------------------------------
# def mutate_string(string, position, character):
#     con=list(string)
#     con[position]=character
#     return "".join(con)
#
# if __name__ == '__main__':
#     s = input("enter")
#     i, c = input("enter1").split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)
# ======================================================================
#SUM OF THE ELEMENTS AND THEN AVERAGE THE LIST OF VALUES OF GIVEN NAME IN DICTIONARY
# if __name__ == '__main__':
#     n = int(input("n"))
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input("name_marks").split()
#         print(name,line)
#         scores = list(map(float, line))#convert line to float use map function because map function takes function and iterator
#         student_marks[name] = scores # here float is a function and make a list
#     query_name = input("name")
#     list_marks=student_marks[query_name]
#     addition_marks=sum(list_marks)/len(list_marks)
#     print("{:.2f}".format(addition_marks))
# =========================================================================
# REVERSE STRING BY LOOP
# s="rohit"
# str = ""
# for i in s:
#     str = i+str #here we add i to string and result passed in string also but we print i before string for reverse
# print(str) #so that i add before string and char inside string is move right side
# ------------------------------------------------------------
# MIN AND MAX USE OF axis=0, axis =1 FROM MAP(int,input()), YOU CAN TAKE MANY OR ONE ARGS FROM USER
# YOU CAN ALSO MAKE A LIST FROM MAP FUNCTION IN ONE LINE CODE
# import numpy as np
# N,M=input("row and column").split()
# for i in range(int(N)): #WE CAN WRITE THIS TYPE ALSO arr=np.array([list(map(int,input("num").split())) for i in range(int(N))])
#     arr=np.array([list(map(int,input("num").split()))])
# print(np.max(np.min(arr,axis=1)))
# -----------------------------------------------------------
# N,M=input("row and column").split()
# print(np.max(np.min(np.array([list(map(int,input("num").split())) for i in range(int(N))]),axis=1)))
# -----------------------------22222222222222222222222222------------------
# MIN AND MAX
# arr=[]
# n,m=map(int,input().split())
# for row in range(n):
#     my_arr=list(map(int,input().split()))
#     arr.append(my_arr)
# my_array=np.array(arr)
# result=np.min(my_array, axis = 1)
# print(max(result))
# ----------------------------3333333333333333333333333-------------------
import re   #input 100,000,000.000
# res=re.compile(r'\D+')
# print("\n".join(re.split(res,input("enter the string"))))
# ---------------------------------------------------------------------------
# Print the first occurrence of the repeating character. If there are no repeating characters, print -1.
# INPUT..12345678910111213141516171820212223 OUTPUT 111
# import re
# m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
# print(m.group(1) if m else -1) #here we used 1 in group for indexing value
# ------------------------------------------------------------------
# vowels is between consonants flags=re.IGNORECASE IS use for to ignore capital or small(if you take samll then it ignore capital)and give output
# import re
# v = "aeiou"
# c = "qwrtypsdfghjklzxcvbnm"
# m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags=re.IGNORECASE)
# if m==[]:
#     print(-1)
# else:
#     for i in m:
#         print(i)
# ------------------------------------------------------------------------
# import re
# m=re.search(r'\d+','1234')
# print(m.end())
# print(m.start())
# """OUTPUT string=aaadaa,substring=aa
# (0, 1)
# (1, 2)
# (4, 5)"""
# import re
# string = input()
# substring = input()
# pattern = re.compile(substring)
# match = pattern.search(string)
# if not match:
#     print('(-1, -1)')
# while match:
#     print('({0}, {1})'.format(match.start(), match.end() - 1))
#     match = pattern.search(string, match.start() + 1) #(that line is just pass the value to upper line)
# ---------------------------------------------------------
# COMMANDS AND OPERATION WITH LIST
# if __name__ == '__main__':
#     n = int(input().strip())
#     Lis = []
#     for t in range(n):
#         args = input().strip().split()
#         if args[0] == "append":
#             Lis.append(int(args[1]))
#         elif args[0] == "insert":
#             Lis.insert(int(args[1]), int(args[2]))
#         elif args[0] == "remove":
#             Lis.remove(int(args[1]))
#         elif args[0] == "pop":
#             Lis.pop()
#         elif args[0] == "sort":
#             Lis.sort()
#         elif args[0] == "reverse":
#             Lis.reverse()
#         elif args[0] == "print":
#             print(Lis)
# ------------------------------------------------------------------------
# PRINT HASH VALUE
# n=int(input())
# print(hash(tuple(map(int,input().split()))))
# ------------------------------------------------------------------------------
# The first line contains X, the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains N, the number of customers.
# The next N lines contain the space separated values of the shoes size  desired by the customer and xi, the price of the shoe.
# --------------------------------------------------------------------------------------
#  from collections import *
# numShoes = int(input('enter'))
# sizes_list = Counter(map(int,input('enter').split()))
# n_cx = int(input('enter'))
# earned = 0
# for i in range(n_cx):
#     size, price = map(int,input('enter').split()) #if we use two variable to the map function, we dont need to pass input to any DS
#     # print(size,price)
#     if sizes_list[size]>0: # sizes_list[size] means we take the value of sizes_list dictionary that is 2 if shoes sizes is 6
#         print(sizes_list[size])
#         earned = earned+ price
#         sizes_list[size] = sizes_list[size]- 1
# print(earned)
# ---------------------------------------------------------------------------------
# input='HackerRank.com presents "Pythonist 2"' output ='hACKERrANK.COM PRESENTS "pYTHONIST 2"'
# means this code will swap lower char to upper
# def swap_case(s):
#     ans = ""
#     for i in s:
#         if i==i.upper():
#             ans=ans+i.lower()
#         else:
#             ans=ans+i.upper()
#     return ans

# if __name__ == '__main__':
#     # 'HackerRank.com presents "Pythonist 2"'
#     s = input()
#     result = swap_case(s)
#     print(result)
# =========================================================================================
# Input :The first line of input contains the original string. The next line contains the substring.
# OUTPUT :Output the integer number indicating the total number of occurrences of the substring in the original string.
# # output is 2
# string = "ininini"
# sub_string = "ini"

# count=0
# for i in range(len(string)):
#     if string[i:len(sub_string)+i]==sub_string:
#         count+=1
# print(count)
# ===================RECURSION METHOD+++++++++++++++++++
# count=0
# def count_substring(string, sub_string):
#     global count
#     if sub_string in string:
#         if (len(string) - 1) <= 1:
#             return count
#         else:
#             cnt_ind = string.find(sub_string)
#             count += 1
#              # cnt_ind+1 to move 1 step ,if i won't give so it will take again & again same char
#             count_substring(string[cnt_ind+1:], sub_string)
#         return count
#     else:
#         return string.count(sub_string)
# if __name__ == '__main__':
#     print(count_substring(string=(input().strip()), sub_string=(input().strip()))) #the vaue us returning to function
# =======================================================================================
