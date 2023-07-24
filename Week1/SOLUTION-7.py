#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a python script to enter any string, replace vowel with its position number.
#22bca29
string = input("Enter a string: ")
new = ''
vowels = 'aeiouAEIOU'
position = 1

for char in string:
    if char in vowels:
        new += str(position)
    else:
        new += char
    position += 1
print("new string number : ", new)

