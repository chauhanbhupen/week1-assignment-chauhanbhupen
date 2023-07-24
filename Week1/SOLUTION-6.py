#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a python script to enter any string and print only part of string. Take input of start character and end character from user.
#22bca29
str = input("Enter a string: ")
first = input("Enter the first character: ")
last = input("Enter the last character: ")

start = str.find(first)
end = str.find(last)

if start != -1 and end != -1:
    remain = str[start:end]
    print("remaining portion of the string:", remain)
else:
    print("Start or end character not found in the string.")

