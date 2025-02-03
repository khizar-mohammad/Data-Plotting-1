#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Birthday_Dictionary = {
    'Person': ['Mahnoor','Faizan','Gabriel','Swatti','Heider'],
    'Birthday': ['5th Nov','6th Nov','5th Nov','6th Nov', '15th Nov']
}

if input("Would you like to append the dictionary? ").lower() == 'y':
  while True:
    name = input("please enter the name ")
    Birthday_Dictionary['Person'].append(name)
    bday = input("Please enter the date of birth ")
    Birthday_Dictionary['Birthday'].append(bday)
    x = input("Would you like to add more? ").lower()
    if x == 'n':
      break

