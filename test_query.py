# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:10:55 2023
LiionDB
@author: lou
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import functions.fn_db as fn_db
import local_db
from sqlalchemy import text
dfndb, db_connection = fn_db.liiondb()

QUERY = '''
        SELECT DISTINCT data.data_id,parameter.symbol,parameter.name as parameter, material.name as material,data.raw_data, parameter.units_output, paper.paper_tag, paper.doi
        FROM data
        JOIN paper ON paper.paper_id = data.paper_id
        JOIN material ON material.material_id = data.material_id
        JOIN parameter ON parameter.parameter_id = data.parameter_id
        WHERE parameter.name = 'half cell ocv'
        AND material.ni > 0.5
        '''
query = text(QUERY)
with dfndb.begin() as conn:
    df = pd.read_sql(query,conn)
df.head(5) #Print top 5 to save space
#%%

local_db, local_db_conn = local_db.localdb()
with local_db.begin() as local_conn:
    df.to_sql('test', local_conn)
    local_conn.execute(text("SELECT * FROM test")).fetchall()
#%%
import local_db
from sqlalchemy import text
local_db, local_db_conn = local_db.localdb()
with local_db.begin() as local_conn:
    # df.to_sql('test', local_conn)
    local_conn.execute(text("alter table test add primary key(data_id);"))
    
