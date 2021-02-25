#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd
from pathlib import Path
from datetime import datetime
from pytz import timezone
tz = timezone('EST')
str2 = datetime.now(tz).strftime('%Y%m%d.%H%M')
dt,uniq_id = str2.split('.')


# In[89]:


tbl_df = pd.read_csv('Table.txt',header=None)
seq_df = pd.read_csv('Seq.txt',header=None)
CT_STR = "USE DATABASE $${flyway:database};\nUSE SCHEMA FACETS_DA_INT;\n\n"


# In[82]:


for index, row in tbl_df.iterrows():
    uniq_id = int(uniq_id) + 1
    if uniq_id%100 > 59: #& uniq_id//100 < 24:
        uniq_id = uniq_id + 100 - uniq_id%100
    #if uniq_id//100 > 24:
    #    uniq_id = 0
    str2 = dt + '.' + str(uniq_id).zfill(4)
    print(str2)
    str1 = row[0].split('.')[1].split(' ')[0]
    filename = "V3.0_"+str2+"__RENAME_TABLE_"+str1+".sql"
    Path(os.path.join("DFiles",str1)).mkdir(parents=True, exist_ok=True)
    f = open(os.path.join("DFiles",str1,filename), 'w')
    f.write(CT_STR)
    f.write(row[0])
    f.write("\n")
    f.close()


# In[90]:


for index, row in seq_df.iterrows():
    uniq_id = int(uniq_id) + 1
    if uniq_id%100 > 59:# & uniq_id//100 < 24:
        uniq_id = uniq_id + 100 - uniq_id%100
    #if uniq_id//100 > 24:
    #    uniq_id = 0
    str2 = dt + '.' + str(uniq_id).zfill(4)
    str1 = row[0].split('.')[1].split(' ')[0]
    str1 = str1.replace('_SEQ','')
    filename = "V3.0_"+str2+"__RENAME_SEQ_"+str1+".sql"
    Path(os.path.join("DFiles",str1)).mkdir(parents=True, exist_ok=True)
    f = open(os.path.join("DFiles",str1,filename), 'w')
    f.write(CT_STR)
    f.write(row[0])
    f.write("\n")
    f.close()

