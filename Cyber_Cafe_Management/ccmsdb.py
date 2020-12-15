#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
"""
Created on Fri Wed 5 02:20:22 2020
Project : Realistics Data Generation For CCMSDB Project To Do Load Test
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
db = 'ccmsdb'
rows = input('Enter the no of records you want to insert.')

def phone_number(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def tblusers():
    EntryID = phone_number(9)
    UserName = fake.first_name() 
    UserAddress = fake.address()
    MobileNumber = phone_number(10)
    Email = UserName + "@gmail.com"
    ComputerName = choice(['Dell', 'ASUS', 'lenvo', 'HP', 'Acer'])
    IDProof = phone_number(9)
    InTime = datetime.fromtimestamp(fake.date_time_between(start_date='-100d', end_date='now').timestamp())
    OutTime = InTime
    Fees = randint(20,100)
    Remark = choice(['Ok', 'Check Out'])
    Status = choice(['In', 'Out'])
    UpdationDate = InTime

    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        tblusers_queery = "INSERT INTO `tblusers`(`EntryID`, `UserName`, `UserAddress`, `MobileNumber`, `Email`, `ComputerName`, `IDProof`, `InTime`, `OutTime`, `Fees`, `Remark`, `Status`, `UpdationDate`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(tblusers_queery,(EntryID, UserName, UserAddress, MobileNumber, Email, ComputerName, IDProof, InTime, OutTime, Fees, Remark, Status, UpdationDate))
        connection.commit()
    except: 
        None
        
        
def tblcomputers():
    ComputerName = choice(['Dell', 'ASUS', 'lenvo', 'HP', 'Acer'])
    ComputerLocation = "Cabin" + str(phone_number(3))
    IPAdd = "127.0.0." + str(phone_number(4))
    EntryDate = datetime.fromtimestamp(fake.date_time_between(start_date='-100d', end_date='now').timestamp())

    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        tblcomputers_queery = "INSERT INTO `tblcomputers`(`ComputerName`, `ComputerLocation`, `IPAdd`, `EntryDate`) VALUES (%s,%s,%s,%s)"
        cursor.execute(tblcomputers_queery,(ComputerName, ComputerLocation, IPAdd, EntryDate))
        connection.commit()
    except: 
        None   
        
        
        
for i in range(0, int(rows)):
    print("{} Records Inserted.".format(i))
    tblcomputers()      
    tblusers()


# In[32]:





# In[36]:


tblcomputers()


# In[22]:


print(datetime.fromtimestamp(fake.date_time_between(start_date='-100d', end_date='now').timestamp()))


# In[ ]:




