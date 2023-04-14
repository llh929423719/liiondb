# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 17:48:20 2023
full copy dfn_db to local
@author: lou
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import functions.fn_db as fn_db
import local_db
from sqlalchemy import text
import qnap_db

tabel_name_list = ['data','parameter','paper','method','data_method','material']
dfndb_engine, db_connection_dic = fn_db.liiondb()
qnap_engine,qnap_db_dic = qnap_db.qnapdb()
for tabel_name in tabel_name_list:
    with dfndb_engine.begin() as conn:
        df = pd.read_sql(text("SELECT * FROM {}".format(tabel_name)),conn)
#%%

# pk = 'paper_id'
    with qnap_engine.begin() as qnap_conn:
        df.to_sql(tabel_name, qnap_conn)
        # qnap_conn.execute(text("alter table {} add primary key({});".format(
        #     tabel_name, pk)))


