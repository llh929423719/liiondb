# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:10:20 2023
qnap db connect
@author: lou
"""

from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
def test():
    print('hello')
    
def qnapdb():
    db_connection_dic = {
    'address' : '192.168.5.100',
    'port' : '3307',
    'username' : 'lou',
    'password' : 'wobushi2b',
    'dbname' : 'dfndb_copy'}
    db_connection_dic = sqlalchemy_connect(db_connection_dic) #Make connection
    db_engine = db_connection_dic['dbobject']
    return db_engine, db_connection_dic

def sqlalchemy_connect(db_connection_dic):
    marriadb_str = ('mysql+pymysql://{username}:{password}@{ipaddress}:{port}/{dbname}'
       .format(username=db_connection_dic['username'],
               password=db_connection_dic['password'],
               ipaddress=db_connection_dic['address'],
               port=db_connection_dic['port'],
               dbname=db_connection_dic['dbname']))
    db_engine = create_engine(marriadb_str)
    db_connection_dic['dbobject']=db_engine
    return db_connection_dic

if __name__ == '__main__':
    test()
    test_engine,test_db_dic = qnapdb()
    with test_engine.begin() as conn:
        conn.execute(text("SELECT * FROM test")).fetchall()
        df = pd.read_sql(text("SELECT * FROM test"),conn)