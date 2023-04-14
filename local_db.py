# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 18:53:39 2023
local db connect
@author: lou
"""

from sqlalchemy import create_engine

def test():
    print('hello')
    
def localdb():
    db_connection_dic = {
    'address' : 'localhost',
    'port' : '5432',
    'username' : 'lou',
    'password' : 'wobushi2b',
    'dbname' : 'postgres'}
    db_connection_dic = sqlalchemy_connect(db_connection_dic) #Make connection
    db_engine = db_connection_dic['dbobject']
    return db_engine, db_connection_dic

def sqlalchemy_connect(db_connection_dic):
    postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'
       .format(username=db_connection_dic['username'],
               password=db_connection_dic['password'],
               ipaddress=db_connection_dic['address'],
               port=db_connection_dic['port'],
               dbname=db_connection_dic['dbname']))
    db_engine = create_engine(postgres_str)
    db_connection_dic['dbobject']=db_engine
    return db_connection_dic