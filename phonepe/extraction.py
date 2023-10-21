import git
import os
import json
import pandas as pd

#GIT CLONING

repository_url = "https://github.com/PhonePe/pulse.git"

destination_directory = "/Users/admin/Desktop/phonepe"

repo = git.Repo.clone_from(repository_url, destination_directory)

#EXTRACTION OF DATA FROM JSON

path_1="/Users/admin/Desktop/phonepe/data/aggregated/transaction/country/india/state"
Agg_trans_state_list = os.listdir(path_1)
Agg_tra = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [], 'Transaction_amount': []}
Agg_trans_state_list
for i in Agg_trans_state_list:
    if i !=".DS_Store":
        p_i=path_1+"/"+i
        Agg_yr = os.listdir(p_i)
        for j in Agg_yr:
            if j !=".DS_Store":
                p_j = p_i +"/"+j
                Agg_yr_list = os.listdir(p_j)
                for k in Agg_yr_list:
                    if k!="20221.json":
                        p_k = p_j + "/"+ k
                        Data = open(p_k,'r')
                        A = json.load(Data)
                        for l in A['data']['transactionData']:
                            Name = l['name']
                            count = l['paymentInstruments'][0]['count']
                            amount = l['paymentInstruments'][0]['amount']
                            Agg_tra['State'].append(i)
                            Agg_tra['Year'].append(j)
                            Agg_tra['Quarter'].append(int(k.strip('.json')))
                            Agg_tra['Transaction_type'].append(Name)
                            Agg_tra['Transaction_count'].append(count)
                            Agg_tra['Transaction_amount'].append(amount)


                

            

df_aggregated_transaction = pd.DataFrame(Agg_tra)


path_2="/Users/admin/Desktop/phonepe/data/aggregated/user/country/india/state"
Agg_user_state_list = os.listdir(path_2)
Agg_user = {'State': [], 'Year': [], 'Quarter': [], 'Brands': [], 'User_Count': [], 'User_Percentage': []}
for i in Agg_user_state_list:
    if i !=".DS_Store":
        p_i=path_2+"/"+i
        Agg_yr = os.listdir(p_i)
        for j in Agg_yr:
            if j !=".DS_Store":
                p_j = p_i +"/"+j
                Agg_yr_list = os.listdir(p_j)
                for k in Agg_yr_list:
                    if k!="20221.json":
                        p_k = p_j + "/"+ k
                        Data = open(p_k,'r')
                        B= json.load(Data)
                        try:
                            for l in B["data"]["usersByDevice"]:
                                brand_name = l["brand"]
                                count_ = l["count"]
                                ALL_percentage = l["percentage"]
                                Agg_user["State"].append(i)
                                Agg_user["Year"].append(j)
                                Agg_user["Quarter"].append(int(k.strip('.json')))
                                Agg_user["Brands"].append(brand_name)
                                Agg_user["User_Count"].append(count_)
                                Agg_user["User_Percentage"].append(ALL_percentage*100)
                        except:
                            pass
            
            
            
            
df_aggregated_user = pd.DataFrame(Agg_user)
                
df_aggregated_user 

path_3 = "/Users/admin/Desktop/phonepe/data/map/transaction/hover/country/india/state"
map_tra_state_list = os.listdir(path_3)
map_tra = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Transaction_Count': [], 'Transaction_Amount': []}
for i in map_tra_state_list:
    if i !=".DS_Store":
        p_i=path_3+"/"+i
        map_yr = os.listdir(p_i)
        for j in map_yr:
            if j !=".DS_Store":
                p_j = p_i +"/"+j
                map_yr_list = os.listdir(p_j)
                for k in map_yr_list:
                    if k!="20221.json":
                        p_k = p_j + "/"+ k
                        Data = open(p_k,'r')
                        C= json.load(Data)
                        for l in C["data"]["hoverDataList"]:
                            District = l["name"]
                            count = l["metric"][0]["count"]
                            amount = l["metric"][0]["amount"]
                            map_tra['State'].append(i)
                            map_tra['Year'].append(j)
                            map_tra['Quarter'].append(int(k.strip('.json')))
                            map_tra["District"].append(District)
                            map_tra["Transaction_Count"].append(count)
                            map_tra["Transaction_Amount"].append(amount)
                        
df_map_transaction = pd.DataFrame(map_tra)
df_map_transaction

path_4="/Users/admin/Desktop/phonepe/data/map/user/hover/country/india/state"
map_user_state_list = os.listdir(path_4)
map_user = {"State": [], "Year": [], "Quarter": [], "District": [], "Registered_User": []}
for i in map_user_state_list:
    p_i=path_4+"/"+i
    map_yr = os.listdir(p_i)
    for j in map_yr:
        p_j = p_i +"/"+j
        map_yr_list = os.listdir(p_j)
        for k in map_yr_list:
            p_k = p_j + "/"+ k
            Data = open(p_k,'r')
            D= json.load(Data)
            for l in D["data"]["hoverData"].items():
                district = l[0]
                registereduser = l[1]["registeredUsers"]
                map_user['State'].append(i)
                map_user['Year'].append(j)
                map_user['Quarter'].append(int(k.strip('.json')))
                map_user["District"].append(district)
                map_user["Registered_User"].append(registereduser)
df_map_user = pd.DataFrame(map_user) 
df_map_user

path_5="/Users/admin/Desktop/phonepe/data/top/transaction/country/india/state"
top_tra_state_list = os.listdir(path_5)
top_tra = {'State': [], 'Year': [], 'Quarter': [], 'District_Pincode': [], 'Transaction_count': [], 'Transaction_amount': []}
for i in top_tra_state_list:
    p_i=path_5+"/"+i
    top_yr = os.listdir(p_i)
    for j in top_yr:
        p_j = p_i +"/"+j
        top_yr_list = os.listdir(p_j)
        for k in top_yr_list:
            p_k = p_j + "/"+ k
            Data = open(p_k,'r')
            E= json.load(Data)
            for l in E['data']['pincodes']:
                Name = l['entityName']
                count = l['metric']['count']
                amount = l['metric']['amount']
                top_tra['State'].append(i)
                top_tra['Year'].append(j)
                top_tra['Quarter'].append(int(k.strip('.json')))
                top_tra['District_Pincode'].append(Name)
                top_tra['Transaction_count'].append(count)
                top_tra['Transaction_amount'].append(amount)

df_top_transaction = pd.DataFrame(top_tra)

df_top_transaction


path_6="/Users/admin/Desktop/phonepe/data/top/user/country/india/state"
top_user_state_list = os.listdir(path_6)
top_user = {'State': [], 'Year': [], 'Quarter': [], 'District_Pincode': [], 'Registered_User': []}
for i in top_user_state_list:
    p_i=path_6+"/"+i
    top_yr = os.listdir(p_i)
    for j in top_yr:
        p_j = p_i +"/"+j
        top_yr_list = os.listdir(p_j)
        for k in top_yr_list:
            p_k = p_j + "/"+ k
            Data = open(p_k,'r')
            F= json.load(Data)
            for l in F['data']['pincodes']:
                Name = l['name']
                registeredUser = l['registeredUsers']
                top_user['State'].append(i)
                top_user['Year'].append(j)
                top_user['Quarter'].append(int(k.strip('.json')))
                top_user['District_Pincode'].append(Name)
                top_user['Registered_User'].append(registeredUser)
df_top_user = pd.DataFrame(top_user)
df_top_user


#LOADING DATA TO SQL

import sqlite3
sqlite_db_file ="youE.db"
sqlite_conn = sqlite3.connect(sqlite_db_file)
sqlite_cursor = sqlite_conn.cursor()
agg_tran_table = '''CREATE TABLE IF NOT EXISTS agg_tran(
                         State TEXT ,
                         Year TEXT,
                         Quarter INTEGER,
                        Transaction_type TEXT,
                        Transaction_count INTEGER,
                        Transaction_amount INTEGER)'''
agg_user_table = '''CREATE TABLE IF NOT EXISTS agg_user(
                         State TEXT ,
                         Year TEXT,
                         Quarter INTEGER,
                         Brands TEXT,
                         User_Count INTEGER ,
                         User_Percentage INTEGER)'''
map_tran_table= '''CREATE TABLE IF NOT EXISTS map_tran(
                         State TEXT ,
                         Year TEXT,
                         Quarter INTEGER,
                         District TEXT,
                        Transaction_count INTEGER,
                        Transaction_amount INTEGER)'''

map_user_table='''CREATE TABLE IF NOT EXISTS map_user(
                         State TEXT ,
                         Year TEXT,
                         Quarter INTEGER,
                         District TEXT,
                         Registered_User INTEGER)'''
top_tran_table='''CREATE TABLE IF NOT EXISTS top_tran(
                         State TEXT ,
                         Year TEXT,
                         Quarter INTEGER,
                       District_Pincode TEXT,
                        Transaction_count INTEGER,
                        Transaction_amount INTEGER)'''
top_user_table='''CREATE TABLE IF NOT EXISTS top_user(
                         State TEXT ,
                         Year TEXT,
                         Quarter INTEGER,
                         District_Pincode TEXT,
                         Registered_User INTEGER)'''

sqlite_cursor.execute(agg_tran_table)
sqlite_cursor.execute(agg_user_table)
sqlite_cursor.execute(map_tran_table)
sqlite_cursor.execute(map_user_table)
sqlite_cursor.execute(top_tran_table)
sqlite_cursor.execute(top_user_table)



sqlite_conn.commit()

#Agg_tra

agg_tran_insert="INSERT INTO agg_tran(State,Year,Quarter,Transaction_type,Transaction_count,Transaction_amount) VALUES(?,?,?,?,?,?)"
values=tuple(Agg_tra.values())
values1=[]
for i in values:
    values1.append(tuple(i))
i=0
count=len(values1[0])
while i<count:
    values2=[]
    for h in range(len(values1)):
        values2.append(values1[h][i])
    values3=tuple(values2)
    i+=1
    sqlite_cursor.execute(agg_tran_insert,values3)
    sqlite_conn.commit()


Agg_user_insert="INSERT INTO agg_user(State,Year,Quarter,Brands,User_Count ,User_Percentage) VALUES(?,?,?,?,?,?)"
values=tuple(Agg_user.values())
values1=[]
for i in values:
    values1.append(tuple(i))
i=0
count=len(values1[0])
while i<count:
    values2=[]
    for h in range(len(values1)):
        values2.append(values1[h][i])
    values3=tuple(values2)
    i+=1
    sqlite_cursor.execute(Agg_user_insert,values3)
    sqlite_conn.commit()

map_tran_insert="INSERT INTO map_tran( State ,Year,Quarter,District,Transaction_count,Transaction_amount) VALUES(?,?,?,?,?,?)"
values=tuple(map_tra.values())
values1=[]
for i in values:
    values1.append(tuple(i))
i=0
count=len(values1[0])
while i<count:
    values2=[]
    for h in range(len(values1)):
        values2.append(values1[h][i])
    values3=tuple(values2)
    i+=1
    sqlite_cursor.execute(map_tran_insert,values3)
    sqlite_conn.commit()

map_user_insert="INSERT INTO map_user(State,Year,Quarter,District,Registered_User) VALUES(?,?,?,?,?)"
values=tuple(map_user.values())
values1=[]
for i in values:
    values1.append(tuple(i))
i=0
count=len(values1[0])
while i<count:
    values2=[]
    for h in range(len(values1)):
        values2.append(values1[h][i])
    values3=tuple(values2)
    i+=1
    sqlite_cursor.execute(map_user_insert,values3)
    sqlite_conn.commit()

top_tran_insert="INSERT INTO top_tran(State,Year,Quarter,District_Pincode,Transaction_count,Transaction_amount)VALUES(?,?,?,?,?,?)"
values=tuple(top_tra.values())
values1=[]
for i in values:
    values1.append(tuple(i))
i=0
count=len(values1[0])
while i<count:
    values2=[]
    for h in range(len(values1)):
        values2.append(values1[h][i])
    values3=tuple(values2)
    i+=1
    sqlite_cursor.execute(top_tran_insert,values3)
    sqlite_conn.commit()

top_user_insert="INSERT INTO top_user(State,Year,Quarter,District_Pincode,Registered_User)VALUES(?,?,?,?,?)"
values=tuple(top_user.values())
values1=[]
for i in values:
    values1.append(tuple(i))
i=0
count=len(values1[0])
while i<count:
    values2=[]
    for h in range(len(values1)):
        values2.append(values1[h][i])
    values3=tuple(values2)
    i+=1
    sqlite_cursor.execute(top_user_insert,values3)
    sqlite_conn.commit()