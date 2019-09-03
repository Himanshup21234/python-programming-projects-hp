#!/usr/bin/env python
# coding: utf-8

# # AWS DOWNLOAD Script
# 
# This Script is used to Download file from AWS S3 using input File ID as the user input and unzip files in a directory.

# In[1]:


import os as os
import logging as log
from collections import defaultdict
import boto3
from datetime import datetime
import time as time
import awscli
import logging
# !pip install unrar
# !pip install rarfile.
#import zip file.
import zipfile
# import rarfile
import os


# ## Logging Initialization
# 
# Standard Library Logging Module. Python comes with a logging module in the standard library which provides a flexible framework for emitting log messages from Python programs. This module is widely used by libraries and is the first go-to point for most programmers when it comes to logging.

# In[2]:


LOG_FILENAME='logging_aws_download_script_' + str(datetime.now().strftime('%d_%m_%Y')) + '.log'
# print(LOG_FILENAME)
# Set up a specific logger with our desired output level
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(lineno)d %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=LOG_FILENAME,
                    filemode='w')
#Creating an object
#Setting the threshold of logger to DEBUG 
my_logger = logging.getLogger('DOWNLOAD')
my_logger.setLevel(logging.DEBUG)
f_handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=1000000, backupCount=100)
my_logger.addHandler(f_handler)


# ## Initializing AWS S3 bucket

# In[3]:


# INIT PARAM
my_logger.info("Initialising AWS S3 bucket connection through IAM security.")
dirName='D:\\S3 Buckets\\'
#my_logger.info('Initialising AWS S3 bucket connection through IAM security.')
try:
    ACCESS_KEY_ID = ''
    ACCESS_SECRET_KEY = ''
    s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY_ID,aws_secret_access_key=ACCESS_SECRET_KEY,region_name='ap-south-1',verify=False)
    if s3:
#         print('done')
        my_logger.info("AWS S3 Session Created.")
        my_logger.warning("SSL Verification: False")
except Exception as error:
#     print("Not Fetched")
    my_logger.error("AWS S3 Session Failed.")


# ## Directory Exploring
# 
# Funcitons created for Directory Checking:
# <br><font color=red><b>check_create_directory()</b></font></br>
# <br><font color=red><b>file_check()</b></font></br>

# In[11]:


def check_create_directory():
    my_logger.info("#Module check_create_directory started")
        # Create directory
    for bucket_dir in BUCKET_TREE:
        dirfolder=os.path.join(dirName,bucket_dir)
        my_logger.info("Directory to be checked: %s",dirfolder)
#         print(dirfolder)
        if os.path.exists(dirName):
            my_logger.info("Directory %s Exist",dirName)
#             print("Directory",dirName,"Exist")
            if os.path.exists(dirfolder):
                # Create target Directory
                my_logger.info("Directory %s Exist",dirfolder)
#                 print("Directory " , dirfolder ,  "Exist ")      
            # Create target Directory if don't exist
            elif not os.path.exists(dirfolder):
                os.mkdir(dirfolder)
                my_logger.info("Directory %s Created",dirfolder)
#                 print("Directory " , dirfolder ,  " Created ")
            else:
                my_logger.error('Directory %s failed to Created',dirfolder)
#                 print("Directory " , dirfolder ,  " failed to Created")
        else:
            my_logger.error("Directory %s doesn't exist",dirName)
#             print("Directory doesn't exist",dirName)
    my_logger.info("#Module check_create_directory finished")

        
def file_check(bucket,filename):
    my_logger.info("#Module file_check started")
#     print("Check1")
    dirCheck=os.path.join(dirName,bucket)
    my_logger.info("Inside Directory %s",dirCheck)
#     print(dirCheck)
    loc=os.path.join(dirCheck,filename)
#     print(loc)
    if os.path.exists(dirCheck) and os.path.isdir(dirCheck):
        if not os.listdir(dirCheck):
            my_logger.debug("Directory is empty %s",dirCheck)
#             print("Directory is empty")
            my_logger.info("Calling Module AWS_download")
            AWS_download(bucket,filename)
            my_logger.debug("For loc %s Calling Module check_archive_file", loc)
            check_archive_file(loc)
        else:
            my_logger.info("Directory is not empty")
#             print("Directory is not empty")
            for file in os.listdir(dirCheck):
                loc1=os.path.join(dirCheck,file)
                my_logger.debug("Location for unzip %s",loc1)
#                 print("Location for unzip",loc1)
#                 print(file)
#                 print(filename)
                if file.split('.zip')[0] == filename.split('.zip')[0]:
                        my_logger.debug("File Already Exist: %s",file)
#                         print("File Already Exist")
                else:
                    my_logger.debug("File doesn't Exist: %s",file)
#                     print("File Doesn't Exist")
                    my_logger.info("Calling Module AWS_download")
                    AWS_download(bucket,filename)
                    my_logger.info("Calling Module check_archive_file")
                    check_archive_file(loc1)
    else:
#         print("Given Directory don't exists")
          my_logger.error("Given Directory don't exists %s", dirCheck)
    my_logger.info("#Module file_check finished")


# ## AWS Exploring
# 
# Funcitons created for Directory Checking:
# <br><font color=red><b>AWS_bucket_structure()</b></font></br>
# <br><font color=red><b>AWS_download_check()</b></font></br>
# <br><font color=red><b>AWS_download()</b></font></br>

# In[10]:


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
            my_logger.info("Total AWS Buckets: %s",objSum)
        # print(BUCKET_NAME)
        #List of Files in Buckets
        for bucket in BUCKET_LIST:
            BUCKET_TREE[bucket]=None
            listObjSummary = s3.Bucket(bucket).objects.all()
    #         print('Items inside: ',bucket)
            for objSum in listObjSummary:
                File_name=objSum.key
                BUCKET_TREE[bucket]=File_name
    except Exception as error:
#         print(error)
        my_logger.error("Exception Error : %s",error)
    my_logger.info("#Module AWS_bucket_structure Finished.")
    return BUCKET_TREE
        
def AWS_download_check(user_inp):
    my_logger.info("#Module AWS_download_check Started.")
    for bucket in BUCKET_TREE:
        listObjSummary = s3.Bucket(bucket).objects.all()
        my_logger.info("Items inside: %s",bucket)
#         print('Items inside: ',bucket)
        for objSum in listObjSummary:
            File_name=objSum.key
            srno=File_name.split('.')[1]
            if srno==user_inp:
                file_check(bucket,File_name)
                my_logger.debug("File with SEQ ID to be picked: %s", File_name)
    my_logger.info("#Module AWS_download_check Finished.")

def AWS_download(BUCKET,DOWN_FILE_NAME):
    my_logger.info("#Module AWS_download_check Started.")
#     s3.Bucket(BUCKET).download_file(DOWN_FILE_NAME,f'C:\Users\1210656\Videos\S3 Buckets\{BUCKET}\{DOWN_FILE_NAME}')
    try:
        s3.Object(BUCKET, DOWN_FILE_NAME).download_file(f'D:\S3 Buckets\{BUCKET}\{DOWN_FILE_NAME}')
    except Exception as error:
        my_logger.error("Error Occured while Downloading: %s", error)
    my_logger.info("#Module AWS_download_check Finished.")


# ## Unzipping Files
# <font color=red><b>check_archive_file()</b></font></br>
# <br><font color=red><b>extractzip()</b></font></br>
# <br>check the file is an archive file or not.</br>
# <br>if the file is an archive file just extract it using the proper extracting method.</br>

# In[7]:


def check_archive_file(loc):
    my_logger.info("#Module check_archive_file Started.")
    # check if it is a zip file or not.
#     print(loc)
    if (loc.endswith('.zip') or loc.endswith('.rar') or loc.endswith('.7z')):
        my_logger.info("File have any archive structure.")
        # chcek the file is present or not .
        if os.path.isfile(loc):
            #create a directory at the same location where file will be extracted.
            output_directory_location = loc.split('.zip')[0]
            # if os path not exists .
            if not os.path.exists(output_directory_location):
                # create directory .
                my_logger.debug("Extracting Directory doesn't exist: %s",output_directory_location)
                my_logger.debug("Creating Extracting Directory : %s",output_directory_location)
                os.mkdir(output_directory_location)
#                 print(" Output Directory " , output_directory_location)
                # extract 
                if loc.endswith('.zip'):
                    my_logger.info("Extracting File is in Zip format.")
                    extractzip(loc,output_directory_location)
                elif loc.endswith('.rar'):
                    my_logger.info("Extracting File is in Rar format.")
                    extractrar(loc,output_directory_location)
                else:
                    my_logger.info("Extracting File is in 7z format.")
                    extract7z(loc,output_directory_location)
            else:
                # Directory allready exist.
                my_logger.info("Output Directory already exist: %s ",output_directory_location)
#                 print("Output Directory already exist " , output_directory_location)
        else:
            my_logger.info("File not located to this path")
#             print("File not located to this path")
    else:
        my_logger.info("File do not have any archive structure.")
#         print("File do not have any archive structure.")
    my_logger.info("#Module check_archive_file Finsihed.")

def extractzip(loc,outloc):
    '''
    using the zipfile tool extract here .
    This function is valid if the file type is zip only
   '''
    my_logger.info("#Module extractzip Started.")
    with zipfile.ZipFile(loc,"r") as zip_ref:
        my_logger.info("Iterate over zip info list.")
        # iterate over zip info list.
        for item in zip_ref.infolist():
            zip_ref.extract(item,outloc)
        # once extraction is complete
        my_logger.info("Check if the files contains any zip file or not")
        # check the files contains any zip file or not .
        # if directory then go through the directoty.
        zip_files = [files for files in zip_ref.filelist if files.filename.endswith('.zip')]
        # print other zip files
        # print(zip_files)
        # iterate over zip files.
        for file in zip_files:
            # iterate to get the name.
            my_logger.info("Files contains any zip files:",file)
            new_loc = os.path.join(outloc,file.filename)
            #new location
            # print(new_loc)
            #start extarction.
            my_logger.info("Calling Module check_archive_file.")
            check_archive_file(new_loc)
        # close.
        zip_ref.close()
        my_logger.info("#Module extractzip Finished.")


# In[12]:


my_logger.info("######################Started Main function#####################")
if __name__ == '__main__':
    BUCKET_TREE= {}
    BUCKET_TREE=AWS_bucket_structure()
    check_create_directory()
    my_logger.info("Input Entered")
    user_inp=input("Enter the file ID:")
    my_logger.info("Input Entered: %s",user_inp)
    my_logger.info("Module AWS_download_check Calling.")
    AWS_download_check(user_inp)
my_logger.info("#####################Finished Main function#######################")
