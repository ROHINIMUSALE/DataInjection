#!/usr/bin/env python
# coding: utf-8

# In[68]:


# -*- coding: utf-8 -*-
"""
Created on Fri Nov 5 02:20:22 2020
Project : Realistics Data Generation For OES Entrollment System Project To Do Load Test
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

host = '192.168.6.130'
user_db = 'root'
password_db = 'Novi1234'
db = 'osp'
rows = input('Enter the no of records you want to insert.')

def phone_number(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def availability():
    
    bloodgroup = choice(['A+', 'B', 'A', 'O', 'B+', 'AB+','AB-','A-','B-'])
    organization = fake.first_name() + " " + fake.last_name() + " Pvt. Ltd"
    address = fake.address()
    Units = randint(10,250)

    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        availability_queery = "INSERT INTO `availability`(`bloodgroup`, `organization`, `address`, `Units`) VALUES (%s,%s,%s,%s)"
        cursor.execute(availability_queery,(bloodgroup, organization, address, Units))
        connection.commit()
    except: 
        None
        
        
def blood_camps():
    
    name = fake.first_name() + " " + fake.last_name()
    email = name.split()[0] + "@gmail.com"
    number = phone_number(10)
    city = fake.city()
    address = fake.address()
    date = fake.date_between(start_date='-30d',end_date='-20d')
    time = choice(['12 am to 4 pm', '11 am to 3 pm'])

    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        blood_camps_queery = "INSERT INTO `blood camps`( `name`, `email`, `number`, `city`, `address`, `date`, `time`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(blood_camps_queery,(name, email, number, city, address, date, time))
        connection.commit()
    except: 
        None
        
def donors():
    
    name = fake.first_name() + " " + fake.last_name()
    number = phone_number(10)
    bgroup = choice(['A+', 'B', 'A', 'O', 'B+', 'AB+','AB-','A-','B-'])
    address = fake.address()

    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        donors_queery = "INSERT INTO `donors`(`name`, `number`, `bgroup`, `address`) VALUES (%s,%s,%s,%s)"
        cursor.execute(donors_queery,(name, number, bgroup, address))
        connection.commit()
    except: 
        None           
        
def organization():
    
    name = fake.first_name() + " " + fake.last_name() + " Pvt. Ltd"
    city = fake.city()
    address = fake.address()
    number = phone_number(10)
    email = name.split()[0] + "@gmail.com"
    password = name.split()[0] + str(phone_number(4))
    

    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        organization_queery = "INSERT INTO `organization`(`name`, `city`, `address`, `number`, `email`, `password`) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(organization_queery,(name, city, address, number, email, password))
        connection.commit()
    except: 
        None        
        
def sponsers():
    
    name = fake.first_name() + " " + fake.last_name() + " Pvt. Ltd"
    email = name.split()[0] + "@gmail.com"
    password = name.split()[0] + str(phone_number(4))
    

    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        sponsers_queery = "INSERT INTO `sponsers`( `name`, `email`, `password`) VALUES (%s,%s,%s)"
        cursor.execute(sponsers_queery,(name, email, password))
        connection.commit()
    except: 
        None
        
def users():
    
    name = fake.first_name() + " " + fake.last_name() 
    state = fake.state()
    bloodgroup = choice(['A+', 'B', 'A', 'O', 'B+', 'AB+','AB-','A-','B-'])
    number = phone_number(10)
    email = name.split()[0] + "@gmail.com"
    password = name.split()[0] + str(phone_number(4))
    

    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        users_queery = "INSERT INTO `users`(`name`, `state`, `bloodgroup`, `number`, `email`, `password`) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(users_queery,(name, state, bloodgroup, number, email, password))
        connection.commit()
    except: 
        None        
        
for i in range(0, int(rows)):
    print("{} Records Inserted.".format(i))
    availability()
    blood_camps()
    donors()
    organization()
    sponsers()
    users()           


# In[57]:





# In[67]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




