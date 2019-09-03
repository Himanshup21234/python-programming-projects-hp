#!/usr/bin/env python
# coding: utf-8
#python 3.x
import csv
import sys
#convert a "comma separated values" file to vcf contact cards

#USAGE:
#CSV_to_Vcards.py CSV_filename


def convert(somefile):
    #assuming file format : UID,lastname.firstname,phonenumber
    with open( somefile, 'r' ) as source:
        reader = csv.reader( source )
        with open('ALL.vcf', 'w') as allvcf:
            i = 0
            for row in reader:
                #write in individual vcf
                
                firstn=row[1].split()[0]
                lstnm=row[1].split()[-1]
                vcf = open('C:\\Users\\Himanshu Pant\\Downloads\\.ipynb_checkpoints\\' + firstn + lstnm + ".vcf", 'w')
                vcf.write( 'BEGIN:VCARD' + "\n")
                vcf.write( 'VERSION:3.0' + "\n")
                vcf.write( 'N:' + lstnm + ';' + firstn + "\n")
                vcf.write( 'FN:' + firstn + ' ' + lstnm + "\n")
                vcf.write( 'ORG:' + 'ATI' + "\n")
                vcf.write( 'TEL;CELL:' + row[2] + "\n")
                vcf.write( 'UID:' + row[0] + "\n")
                vcf.write( 'END:VCARD' + "\n")
                vcf.write( "\n")
                vcf.close()

                #write in the "ALL.vcf" file
                allvcf.write( 'BEGIN:VCARD' + "\n")
                allvcf.write( 'VERSION:3.0' + "\n")
                allvcf.write( 'N:' + lstnm + ';' + firstn + "\n")
                allvcf.write( 'FN:' + firstn + ' ' + lstnm + "\n")
                allvcf.write( 'ORG:' + 'ATI' + "\n")
                allvcf.write( 'TEL;CELL:' + row[2] + "\n")
                allvcf.write( 'UID:' + row[0] + "\n")
                allvcf.write( 'END:VCARD' + "\n")
                allvcf.write( "\n")

                i += 1#counts
            print (str(i) + " vcf cards generated")
       
convert("Copy of Contact.csv")

