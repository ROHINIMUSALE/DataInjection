#!/usr/bin/env python
# coding: utf-8

# In[19]:


# -*- coding: utf-8 -*-
"""
Created on Fri Wed 5 02:20:22 2020
Project : Realistics Data Generation For Registration And Login Project To Do Load Test
@author: Rohini Musale

"""

from faker import Faker
from pymysql import connect
from pymysql import cursors
from pymysql.cursors import DictCursor
from datetime import datetime
from datetime import timedelta 
from datetime import date
from random import choice, randint
import pandas as pd
import numpy as np


fake = Faker('en_IN')

host = '192.168.0.158'
user_db = 'root'
password_db = 'Novi1234'
db = 'regloginsystem'
rows = input('Enter the no of records you want to insert.')

def phone_number(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)



def users():
    fname = fake.first_name() 
    lname = fake.last_name()
    email = fname + "@gmail.com"
    password = fname + str(phone_number(5))
    contactno = phone_number(10)
    posting_date = datetime.fromtimestamp(fake.date_time_between(start_date='-100d', end_date='now').timestamp())

    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        users_queery = "INSERT INTO `users`(`fname`, `lname`, `email`, `password`, `contactno`, `posting_date`) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(users_queery,(fname, lname, email, password, contactno, posting_date))
        connection.commit()
    except: 
        None
        
for i in range(0, int(rows)):
    print("{} Records Inserted.".format(i))
    users()        


# In[4]:



        
        


# In[17]:


users()


# In[ ]:




