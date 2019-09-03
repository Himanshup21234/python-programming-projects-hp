#!/usr/bin/env python
# coding: utf-8

# # AWS UPLOAD Script
# 
# Script has no inputs. It replicates the directory tree of our Physical system to the AWS cloud S3 tree.

# In[28]:


import os as os
import logging as logging
import boto3 as boto3
import awscli as awscli
from datetime import datetime
import time as time
import sys


# ## For Cleaning Loggers and handlers 

# In[9]:


# logger=logging.getLogger()
# logger.disabled=False
# logging.disable(sys.maxsize)
# logging.disable(logging.NOTSET)
# logging.getLogger().disabled = False
# logger.disabled=False
# for handler in logger.handlers[:]:
#     logger.removeHandler(handler)


# ## Log Initialization

# In[29]:


LOG_FILENAME='logging_aws_upload_script_' + str(datetime.now().strftime('%d_%m_%Y')) + '.log'
print(LOG_FILENAME)
# Set up a specific logger with our desired output level
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(lineno)d %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=LOG_FILENAME,
                    filemode='w')
#Creating an object
#Setting the threshold of logger to DEBUG 
my_logger = logging.getLogger('UPLOAD')
my_logger.setLevel(logging.DEBUG)
f_handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=1000000, backupCount=100)
my_logger.addHandler(f_handler)


# In[30]:


# INIT PARAM
my_logger.info('Initialising AWS S3 bucket connection through IAM security.')
try:
    ACCESS_KEY_ID = ''
    ACCESS_SECRET_KEY = ''
    s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY_ID,aws_secret_access_key=ACCESS_SECRET_KEY,region_name='ap-south-1',verify=False)
    if s3:
        my_logger.info('AWS S3 Session Created.')
        my_logger.warning("SSL Verification: False")
except Exception as error:
    my_logger.error("AWS S3 Session Failed.")
# dataset = {}
dirName='C:\\Users\\1210656\\Pictures\\S3 Buckets'
# print("for loop outside")
# dirName='C:\\Users\\1210656\\Pictures\\rest'


# ## Directory Exploring
# Funcitons created for Directory Checking:
# <br><font color=red><b>check_directory()</b></font></br>
# <br><font color=red><b>directory_extract()</b></font></br>

# In[31]:


#Block for Directory check
def check_directory():
    my_logger.info("#Module check_directory started.")
    # Check if a Directory is empty and also check exceptional situations.  
    if os.path.exists(dirName) and os.path.isdir(dirName):
        if not os.listdir(dirName):
            my_logger.error("%s doesn't exist.",dirName)
            my_logger.info("#Module check_directory finished.")
            return 1
        else:
            my_logger.error("%s exist.",dirName)
            my_logger.info("#Module check_directory finished.")
            return 2
    else:
        my_logger.error("%s doesn't exist.",os.path)
        my_logger.info("#Module check_directory finished.")
        return 3

def directory_extract():
    my_logger.info("#Module directory_extract started.")
    # Recursively read all files
    for root, subFolders, _ in os.walk(dirName):
    #     print("for loop1")
    #     print(root)
    #     print(subFolders)
    #     print(_)
        if len(subFolders):
#             print(len(subFolders))
#             print((subFolders))
    #         print("for loop2")
            for folder in subFolders:
                directory = os.path.join(root, folder)
#                 print(directory)
#                 print(folder)
                BUCKET_NAME=folder
#                 print(BUCKET_NAME,"::",flgchk)
#                 print("Bucket_name",BUCKET_NAME)
#                 if flgchk==1:
                if os.listdir(directory):
                    for r, s, files in os.walk(directory):
    #                     print("inside")
#                         print(s)
#                         print(files)
                        for f in files:
                            UP_FILE_NAME=f
                            filedirectory=directory+'\\'+f
                            my_logger.info("#Module AWS_upload calling.")
                            AWS_upload(BUCKET_NAME,filedirectory,UP_FILE_NAME)
#                             print(f) 
    my_logger.info("#Module directory_extract finished.")


# ## AWS Exploring
# 
# Funcitons created for Directory Checking:
# <br><font color=red><b>AWS_bucket_check()</b></font></br>
# <br><font color=red><b>AWS_bucket_create()</b></font></br>
# <br><font color=red><b>AWS_create_bucket()</b></font></br>
# <br><font color=red><b>AWS_upload()</b></font></br>

# In[42]:


#List of Files in Buckets
def AWS_bucket_structure():
    my_logger.info("#Module AWS_bucket_structure Started.")
    BUCKET_LIST = []
    BUCKET_TREE={}
        #List of Buckets
    try:
        listObj=s3.buckets.all()
        for objSum in listObj:
        #     print(objSum.name)
            BUCKET_LIST.append(objSum.name)
        # print(BUCKET_NAME)
        #List of Files in Buckets
        for bucket in BUCKET_LIST:
            BUCKET_TREE[bucket]=None
            listObjSummary = s3.Bucket(bucket).objects.all()
    #         print('Items inside: ',bucket)
            for objSum in listObjSummary:
                File_name=objSum.key
                BUCKET_TREE[bucket]=File_name
        my_logger.info("#Module AWS_bucket_structure Finished.")
    except Exception as error:
        my_logger.error("Exception Error : %s",error)
    return BUCKET_TREE

def AWS_bucket_check():
    my_logger.info("#Module AWS_bucket_check started.")
    if os.path.exists(dirName):
        for file in os.listdir(dirName):
            print(file)
            my_logger.debug(" Check for Bucket Name: %s ",file)
            AWS_bucket_create(file)
            my_logger.info("#Module AWS_bucket_create calling.")
    my_logger.info("#Module AWS_create_bucket finished.")
            
def AWS_bucket_create(bucket_name):
    my_logger.info("#Module AWS_bucket_create started.")
    if bucket_name in BUCKET_TREE:
        my_logger.info("Found Bucket: %s",bucket_name)
    else:
        print(bucket_name)
        my_logger.info("Not Found Bucket: %s",bucket_name)
        my_logger.info("#Module AWS_create_bucket calling.")
        AWS_create_bucket(bucket_name)
    my_logger.info("#Module AWS_bucket_create started.")
        

def AWS_create_bucket(BUCKET_NAME):
    my_logger.info("#Module AWS_create_bucket started.")
    try:
        first_bucket = s3.create_bucket(Bucket=BUCKET_NAME,ACL='public-read-write',CreateBucketConfiguration={
       'LocationConstraint': 'ap-south-1'})
        my_logger.info("Bucket Created: %s",first_bucket)
    except Exception as error:
        my_logger.error("Exception Error : %s",error)
    my_logger.info("#Module AWS_create_bucket finished.")

#Block for Upload
def AWS_upload(BUCKET_NAME,FILE_NAME,UP_FILE_NAME):
    my_logger.info("#Module AWS_upload started.")
  # Doc Uploaded as Public
    try:
        with open(FILE_NAME, 'rb') as data :
            s3.Bucket(BUCKET_NAME).put_object(Key=UP_FILE_NAME, Body=data)
    #         print("AWS Function Over")
    except Exception as error:
        my_logger.error("Exception Error : %s",error)


# ## Calling Main Function

# In[44]:


my_logger.info("######################Started Main function#####################")
BUCKET_LIST = []
BUCKET_TREE= {}
chk=check_directory()
if chk == 2 :
    my_logger.info("#Started Uploading")
    BUCKET_TREE=AWS_bucket_structure()
    AWS_bucket_check()
    directory_extract()
elif chk ==1:
    my_logger.warning("Directory is empty")
else:
    my_logger.warning("Directory doesn't exists")
my_logger.info("#####################Finished Main function#######################")

