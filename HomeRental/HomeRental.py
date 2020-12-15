#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
"""
Created on Fri Wed 5 02:20:22 2020
Project : Realistics Data Generation For Home Rental Project To Do Load Test
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
db = 'newrent'
rows = input('Enter the no of records you want to insert.')

def phone_number(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def get_userid():
    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db) 
        cursor = connection.cursor(DictCursor)
        sql_getuserid = "SELECT `id` FROM `users`"
        cursor.execute(sql_getuserid)
        result = cursor.fetchall()
        connection.commit()
        return choice(result[:30])
        
    except:
        return """{'id': 7}"""


def users():
    fullname = fake.first_name() + " " + fake.last_name()
    mobile = phone_number(10)
    username = fullname.split()[0] + str(phone_number(2))
    email = username + "@gmail.com"
    password = fullname.split()[0] + str(phone_number(5))
    created_at = datetime.fromtimestamp(fake.date_time_between(start_date='-100d', end_date='now').timestamp())
    updated_at = datetime.fromtimestamp(fake.date_time_between(start_date='-100d', end_date='now').timestamp())
    role = "user"
    status = "1"

    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        users_queery = "INSERT INTO `users`(`fullname`, `mobile`, `username`, `email`, `password`, `created_at`, `updated_at`, `role`, `status`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(users_queery,(fullname, mobile, username, email, password, created_at, updated_at, role, status))
        connection.commit()
    except: 
        None
        
        
def room_rental_registrations_apartment():
    
    uid = get_userid()
    fullname = fake.first_name() + " " + fake.last_name()
    mobile = phone_number(10) 
    alternat_mobile = phone_number(10) 
    email = fullname.split()[0] + "@gmail.com"
    country = fake.country()
    state = fake.state()
    city = fake.city()
    landmark = city
    rent = randint(1000,10000)
    deposit = randint(1000,5000)
    plot_number = randint(21,255)
    apartment_name = fake.first_name() + "Apartment"
    ap_number_of_plats = randint(100,999)
    rooms = choice(['1bhk','2bhk','3bhk'])
    floor = randint(1,15)
    purpose = choice(['Residential','Rental','Flat'])
    own = 'rented'
    area =  str(randint(1,15)) + "sqr feet"
    address = fake.address()
    accommodation = choice(['Wifi','AC','TV','Water'])
    description = choice(['Well','Good','Not Bad','Poor','Bad'])
    image = 'uploads/Jellyfish.jpg'
    open_for_sharing = choice(['Yes','No'])
    other = choice(['None','Rental','Flat','Residential'])
    vacant =  randint(1,4)
    created_at = datetime.fromtimestamp(fake.date_time_between(start_date='-100d', end_date='now').timestamp())
    updated_at = datetime.fromtimestamp(fake.date_time_between(start_date='-100d', end_date='now').timestamp())
    user_id = uid['id']
    user_id = int(user_id)
    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        room_rental_registrations_apartment_queery = "INSERT INTO `room_rental_registrations_apartment`(`fullname`, `mobile`, `alternat_mobile`, `email`, `country`, `state`, `city`, `landmark`, `rent`, `deposit`, `plot_number`, `apartment_name`, `ap_number_of_plats`, `rooms`, `floor`, `purpose`, `own`, `area`, `address`, `accommodation`, `description`, `image`, `open_for_sharing`, `other`, `vacant`, `created_at`, `updated_at`, `user_id`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(room_rental_registrations_apartment_queery,(fullname, mobile, alternat_mobile, email, country, state, city, landmark, rent, deposit, plot_number, apartment_name, ap_number_of_plats, rooms, floor, purpose, own, area, address, accommodation, description, image, open_for_sharing, other, vacant, created_at, updated_at, user_id))
        connection.commit()
    except: 
        None        
        
        

def room_rental_registrations():
    
    uid = get_userid()
    fullname = fake.first_name() + " " + fake.last_name()
    mobile = phone_number(10) 
    alternat_mobile = phone_number(10) 
    email = fullname.split()[0] + "@gmail.com"
    country = fake.country()
    state = fake.state()
    city = fake.city()
    landmark = city
    rent = randint(1000,10000)
    sale = randint(1000,5000)
    deposit = randint(1000,5000)
    plot_number = randint(21,255)
    rooms = choice(['1bhk','2bhk','3bhk'])
    address = fake.address()
    accommodation = choice(['Wifi','AC','TV','Water'])
    description = choice(['Well','Good','Not Bad','Poor','Bad'])
    image = 'uploads/Jellyfish.jpg'
    open_for_sharing = choice(['Yes','No'])
    other = choice(['None','Rental','Flat','Residential'])
    vacant =  randint(1,4)
    created_at = datetime.fromtimestamp(fake.date_time_between(start_date='-100d', end_date='now').timestamp())
    updated_at = datetime.fromtimestamp(fake.date_time_between(start_date='-100d', end_date='now').timestamp())
    user_id =  uid['id']
    user_id = int(user_id)

    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        room_rental_registrations_queery = "INSERT INTO `room_rental_registrations`(`fullname`, `mobile`, `alternat_mobile`, `email`, `country`, `state`, `city`, `landmark`, `rent`, `sale`, `deposit`, `plot_number`, `rooms`, `address`, `accommodation`, `description`, `image`, `open_for_sharing`, `other`, `vacant`, `created_at`, `updated_at`, `user_id`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(room_rental_registrations_queery,(fullname, mobile, alternat_mobile, email, country, state, city, landmark, rent, sale, deposit, plot_number, rooms, address, accommodation, description, image, open_for_sharing, other, vacant, created_at, updated_at, user_id))
        connection.commit()
    except: 
        None        

for i in range(0, int(rows)):
    print("{} Records Inserted.".format(i))
    users()
    room_rental_registrations_apartment()
    room_rental_registrations()              


# In[43]:


get_userid()


# In[ ]:


uid


# In[37]:





# In[ ]:


print(uid)


# In[ ]:




