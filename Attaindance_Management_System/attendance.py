#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
"""
Created on Fri Wed 5 02:20:22 2020
Project : Realistics Data Generation For Attaindance Management System Project To Do Load Test
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
db = 'attendance'
rows = input('Enter the no of records you want to insert.')

def phone_number(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def get_id():
    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db) 
        cursor = connection.cursor(DictCursor)
        sql_getid = "SELECT `id` FROM `employee`"
        cursor.execute(sql_getid)
        result = cursor.fetchall()
        connection.commit()
        return choice(result[:30])
        
    except:
        None 

def users():
    name = fake.first_name()
    username = name + "@gmail.com"
    password = name + str(phone_number(5))
    firstname = name 
    lastname = fake.last_name()

    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        users_queery = "INSERT INTO `users`(`username`, `password`, `firstname`, `lastname`) VALUES (%s,%s,%s,%s)"
        cursor.execute(users_queery,(username, password, firstname, lastname))
        connection.commit()
    except: 
        None
        
        
def employee():
    employee_no = "2020-" + str(phone_number(4))
    firstname = fake.first_name()
    middlename = fake.first_name()
    lastname = fake.last_name()
    department = fake.company()
    position = fake.job()
   
    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        employee_queery = "INSERT INTO `employee`( `employee_no`, `firstname`, `middlename`, `lastname`, `department`, `position`) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(employee_queery,(employee_no, firstname, middlename, lastname, department, position))
        connection.commit()
    except: 
        None        
        
        
        
def attendance():
    eid = get_id()
    employee_id = eid['id']
    log_type = randint(1,4)
    datetime_log = datetime.fromtimestamp(fake.date_time_between(start_date='-100d', end_date='now').timestamp())
    date_updated = datetime.fromtimestamp(fake.date_time_between(start_date='-100d', end_date='now').timestamp())
   
    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        attendance_queery = "INSERT INTO `attendance`(`employee_id`, `log_type`, `datetime_log`, `date_updated`) VALUES (%s,%s,%s,%s)"
        cursor.execute(attendance_queery,(employee_id, log_type, datetime_log, date_updated))
        connection.commit()
    except: 
        None      
        
        
for i in range(0, int(rows)):
    print("{} Records Inserted.".format(i))
    users()
    employee()
    attendance()           


# In[27]:





# In[30]:


attendance()


# In[26]:





# In[ ]:




