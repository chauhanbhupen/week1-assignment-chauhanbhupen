#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a python script to enter any number, if it is integer number, then check its palindrom or not. Print appropriate message if it is not palindrom.
#22BCA29 
n=int(input("Enter number:"))
t=n
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
if(t==r):
    print("the number is a palindrome")
else:
    print("the number isn't a palindrome")

