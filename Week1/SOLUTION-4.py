#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a python script to enter any number, if it is integer number, then check its armstrong or not. Print appropriate message if it is not palindrom.
#22BCA29
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

