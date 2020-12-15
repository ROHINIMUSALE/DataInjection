#!/usr/bin/env python
# coding: utf-8

# In[3]:


# -*- coding: utf-8 -*-
"""
Created on Fri Nov 5 02:20:22 2020
Project : Realistics Data Generation For Usermanagement Project To Do Load Test
@author:Rohini Musale

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

host = '192.168.6.130'
user_db = 'root'
password_db = 'Novi1234'
db = 'armentum'
rows = input('Enter the no of records you want to insert.')

def phone_number(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def get_email():
    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db) 
        cursor = connection.cursor(DictCursor)
        sql_getemail = "SELECT  `email` FROM `users`"
        cursor.execute(sql_getemail)
        result = cursor.fetchall()
        connection.commit()
        return choice(result[:30])
        
    except:
        None 

def users():
    name = fake.first_name() + " " + fake.last_name()
    email = name.split()[0] + "@gmail.com"
    password = name.split()[1] + str(phone_number(5))
    gender = choice(['Male', 'Female'])
    mobile = phone_number(10)
    designation = fake.job()
    status = choice(['1', '0'])

    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        users_queery = "INSERT INTO `users`(`name`, `email`, `password`, `gender`, `mobile`, `designation`, `status`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(users_queery,(name, email, password, gender, mobile, designation, status))
        connection.commit()
    except: 
        None
        
        
def deleteduser():
    deleteemail = get_email()
    email = deleteemail['email']
    deltime = datetime.fromtimestamp(fake.date_time_between(start_date='-100d', end_date='now').timestamp())

    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        deleteduser_queery = "INSERT INTO `deleteduser`(`email`, `deltime`) VALUES (%s,%s)"
        cursor.execute(deleteduser_queery,(email, deltime))
        connection.commit()
    except: 
        None       
        
        
def notification():
    notiuser = fake.first_name() + "@gmail.com"
    notireciver = 'Admin'
    notitype = 'Create Account'
    time = datetime.fromtimestamp(fake.date_time_between(start_date='-100d', end_date='now').timestamp())

    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        notification_queery = "INSERT INTO `notification`(`notiuser`, `notireciver`, `notitype`, `time`) VALUES (%s,%s,%s,%s)"
        cursor.execute(notification_queery,(notiuser, notireciver, notitype, time))
        connection.commit()
    except: 
        None        
        
        
        
def feedback():
    sender = fake.first_name() + "@gmail.com"
    reciver = 'Admin'
    title = choice(['Need to Improve Some Function', 'Amazing', 'Good', 'User can edit their Profile'])
    feedbackdata = choice(['Application is usefull', 'User Can edit their profile', 'Usermangement Application Is Very Amazing for users'])

    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        feedback_queery = "INSERT INTO `feedback`( `sender`, `reciver`, `title`, `feedbackdata`) VALUES (%s,%s,%s,%s)"
        cursor.execute(feedback_queery,(sender, reciver, title, feedbackdata))
        connection.commit()
    except: 
        None

        
for i in range(0, int(rows)):
    print("{} Records Inserted.".format(i))
    users()
    notification()
    feedback()        


# In[20]:





# In[21]:


feedback()


# In[ ]:




