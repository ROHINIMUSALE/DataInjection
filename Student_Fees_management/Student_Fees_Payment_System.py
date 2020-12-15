#!/usr/bin/env python
# coding: utf-8

# # -*- coding: utf-8 -*-
# """
# Created on Fri Nov 5 02:20:22 2020
# Project : Realistics Data Generation For Student Fees Payment System Project To Do Load Test
# @author:Rohini Musale
# 
# """
# 
# from faker import Faker
# from pymysql import connect
# from pymysql import cursors
# from pymysql.cursors import DictCursor
# from datetime import datetime
# from datetime import timedelta 
# from datetime import date
# from random import choice, randint
# import pandas as pd
# import numpy as np
# 
# 
# fake = Faker('en_IN')
# 
# host = '192.168.6.130'
# user_db = 'root'
# password_db = 'Novi1234'
# db = 'sfps_db'
# rows = input('Enter the no of records you want to insert.')
# 
# def phone_number(n):
#     range_start = 10**(n-1)
#     range_end = (10**n)-1
#     return randint(range_start, range_end)
# 
# def get_course():
#     
#     try:
#         connection = connect(host= host, user= user_db, password=password_db, db= db) 
#         cursor = connection.cursor(DictCursor)
#         sql_getcourse = "SELECT `id`, `total_amount` FROM `courses`"
#         cursor.execute(sql_getcourse)
#         result = cursor.fetchall()
#         connection.commit()
#         return choice(result[:30])
#         
#     except:
#         return """{'id': 2,
#         'total_amount': 20000}"""
#     
#     
#     
# def get_studenId():
#     
#     try:
#         connection = connect(host= host, user= user_db, password=password_db, db= db) 
#         cursor = connection.cursor(DictCursor)
#         sql_getstudenId = "SELECT `id` FROM `student`"
#         cursor.execute(sql_getstudenId)
#         result = cursor.fetchall()
#         connection.commit()
#         return choice(result[:30])
#         
#     except:
#         return """{'id': 5}"""   
#     
# def get_student_ef_list():
#     
#     try:
#         connection = connect(host= host, user= user_db, password=password_db, db= db) 
#         cursor = connection.cursor(DictCursor)
#         sql_studenteflist = "SELECT `id` FROM `student_ef_list`"
#         cursor.execute(sql_studenteflist)
#         result = cursor.fetchall()
#         connection.commit()
#         return choice(result[:30])
#         
#     except:
#         return """{'id': 5}"""  
#     
# 
# 
# def students():
#     id_no = phone_number(5)
#     name = fake.first_name() + " " + fake.last_name()
#     email = name.split()[0] + "@gmail.com"
#     contact = phone_number(10)
#     address = fake.address()
#     date_created = fake.date_between(start_date='-30d',end_date='today')
# 
#     try:
#         connection = connect(host= host, user= user_db, password=password_db, db= db)
#         cursor = connection.cursor()
#         students_queery = "INSERT INTO `student`(`id_no`, `name`, `contact`, `address`, `email`, `date_created`) VALUES (%s,%s,%s,%s,%s,%s)"
#         cursor.execute(students_queery,(id_no, name, contact, address, email, date_created))
#         connection.commit()
#     except: 
#         None
#         
# def courses():
#     course = choice(['Computer', 'Mpsc', 'Upsc', 'Banking', 'IT', 'Electrical'])
#     description =  choice(['Its Useful for Future', 'Get Knowledge', 'useful', 'Amazing'])
#     level =  choice(['1', '2', '3'])
#     total_amount = randint(4000,20000)
#     date_created = fake.date_between(start_date='-30d',end_date='today')
# 
#     try:
#         connection = connect(host= host, user= user_db, password=password_db, db= db)
#         cursor = connection.cursor()
#         courses_queery = "INSERT INTO `courses`( `course`, `description`, `level`, `total_amount`, `date_created`) VALUES (%s,%s,%s,%s,%s)"
#         cursor.execute(courses_queery,(course, description, level, total_amount, date_created))
#         connection.commit()
#     except: 
#         None        
#         
#         
# def fees():
#     course_data = get_course()
#     course_id = course_data['id']
#     description =  choice(['Tuition', 'Monthly', 'Full Course'])
#     amount = course_data['total_amount']
# 
#     try:
#         connection = connect(host= host, user= user_db, password=password_db, db= db)
#         cursor = connection.cursor()
#         fees_queery = "INSERT INTO `fees`(`course_id`, `description`, `amount`) VALUES (%s,%s,%s)"
#         cursor.execute(fees_queery,(course_id, description, amount))
#         connection.commit()
#     except: 
#         None        
#         
#         
#         
# def student_ef_list():
#     course_data = get_course()
#     studentId = get_studenId()
#     student_id = studentId['id']
#     ef_no =  phone_number(6)
#     course_id = course_data['id']
#     total_fee = course_data['total_amount']
#     date_created = fake.date_between(start_date='-30d',end_date='today')
# 
#     try:
#         connection = connect(host= host, user= user_db, password=password_db, db= db)
#         cursor = connection.cursor()
#         student_ef_list_queery = "INSERT INTO `student_ef_list`( `student_id`, `ef_no`, `course_id`, `total_fee`, `date_created`) VALUES (%s,%s,%s,%s,%s)"
#         cursor.execute(student_ef_list_queery,(student_id, ef_no, course_id, total_fee, date_created))
#         connection.commit()
#     except: 
#         None            
#         
#         
# def payments():
#     ef_data = get_student_ef_list()
#     ef_id = ef_data['id']
#     amount = randint(1000,20000)
#     remarks = choice(['Good', 'Amazing'])
#     date_created = fake.date_between(start_date='-30d',end_date='today')
# 
#     try:
#         connection = connect(host= host, user= user_db, password=password_db, db= db)
#         cursor = connection.cursor()
#         payments_queery = "INSERT INTO `payments`(`ef_id`, `amount`, `remarks`, `date_created`) VALUES (%s,%s,%s,%s)"
#         cursor.execute(payments_queery,(ef_id, amount, remarks, date_created))
#         connection.commit()
#     except: 
#         None        
#        
#     
# for i in range(0, int(rows)):
#     print("{} Records Inserted.".format(i))
#     students()
#     courses()
#     fees()
#     student_ef_list()
#     payments()
#     

# In[ ]:





# In[69]:



    


# In[70]:


for i in range(0,5):
    students()
    print("{} Inserted.".format(i))


# In[ ]:





# In[ ]:




