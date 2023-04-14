# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:43:58 2023
copy db
@author: lou
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import functions.fn_db as fn_db
import local_db
from sqlalchemy import text
import qnap_db

tabel_name = 'paper'
dfndb_engine, db_connection_dic = fn_db.liiondb()

with dfndb_engine.begin() as conn:
    df = pd.read_sql(text("SELECT * FROM {}".format(tabel_name)),conn)
#%%
qnap_engine,qnap_db_dic = qnap_db.qnapdb()
pk = 'paper_id'
with qnap_engine.begin() as qnap_conn:
    df.to_sql(tabel_name, qnap_conn)
    qnap_conn.execute(text("alter table {} add primary key({});".format(
        tabel_name, pk)))


