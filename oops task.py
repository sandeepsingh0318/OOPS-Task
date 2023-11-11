#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed
#and average_of_vehicle.


# In[2]:


class vehicle():
    def __init__(san,vehicle_name,max_speed,avg_of_vehicle):
        san.vehicle_name=vehicle_name
        san.max_speed=max_speed
        san.avg_of_vehicle=avg_of_vehicle
    def all_details(san):
        return san.vehicle_name,san.max_speed,san.avg_of_vehicle


# In[4]:


Honda=vehicle('Rider',120,55)


# In[5]:


Honda.vehicle_name


# In[6]:


Honda.max_speed


# In[7]:


Honda.avg_of_vehicle


# In[8]:


Honda.all_details()


# In[9]:


#Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
#Create a method named seating_capacity which takes capacity as an argument and returns the name of
#the vehicle and its seating capacity.


# In[40]:


class vehicle():
    def __init__(san,vehicle_name,max_speed,avg_of_vehicle):
        san.vehicle_name=vehicle_name
        san.max_speed=max_speed
        san.avg_of_vehicle=avg_of_vehicle
    def all_details(san):
        return san.vehicle_name,san.max_speed,san.avg_of_vehicle
class car():
     def seating_capacity(san,capacity):
            if capacity<=10:
                return san.vehicle_name
            else:
                pass


# In[41]:


class vehicle(car):
    def __init__(san,vehicle_name,max_speed,avg_of_vehicle):
        san.vehicle_name=vehicle_name
        san.max_speed=max_speed
        san.avg_of_vehicle=avg_of_vehicle
    def all_details(san):
        return san.vehicle_name,san.max_speed,san.avg_of_vehicle


# In[42]:


a=vehicle('i1o',180,15)


# In[43]:


a.seating_capacity(2)


# In[44]:


a.vehicle_name


# In[45]:


a.seating_capacity(4)


# In[46]:


a.vehicle_name


# In[48]:


b=vehicle('innova',200,20)


# In[49]:


b.seating_capacity(7)


# In[50]:


a.seating_capacity(4)


# In[51]:


#Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.


# In[57]:


#sol:- There are two child class and one parent class and the child class inherit the parent class.
#the best example of multiple inheritance is family.
class father():
    def fath_name(san):
        return "my father name is saroj"
class mother():
    def moth_name(san):
        return 'my mother name is Ramwati'
class child(father,mother):
    def parent_name(san):
        return 'i am son of my family'


# In[58]:


sandeep=child()


# In[61]:


sandeep.fath_name()


# In[62]:


sandeep.moth_name()


# In[63]:


sandeep.parent_name()


# In[64]:


#Q4. What are getter and setter in python? Create a class and create a getter and a setter method in 
#this class.


# In[70]:


#sol:- Getter mean to give the permission to access the pravite code by any user.
#Setter mean to give the permission to set the any data in code by any user.they give condition on setter.
class Teacher():
    def __init__(san,name,salary):
        san.name=name
        san.__salary=salary
    @property
    def see_salary(san):
        return san.__salary
    @see_salary.setter
    def modify (san,sal):
        if sal<=34000:
            pass
        else:
            san.__salary=sal


# In[71]:


mp_board=Teacher('Ram sir',34000)


# In[72]:


mp_board.name


# In[73]:


mp_board.see_salary


# In[74]:


mp_board.modify=35000


# In[75]:


mp_board.modify


# In[110]:


#Q5.What is method overriding in python? Write a python code to demonstrate method overriding.
# overriding are not exist in python.only it possible through the classmethod .it mean the __init_function
#override to another function.
class School():
    def __init__(san,name,email):
        san.name=name
        san.email=email
    @classmethod
    def student(sam,name,email):
        return sam(name,email)
    def details(san):
        return san.name,san.email


# In[112]:


san=School.student('VVP','vvp123@gmai.com')


# In[113]:


san.name


# In[114]:


san.email


# In[116]:


san.details()


# In[ ]:




