from google.cloud import bigquery
import os
import google.auth
import pandas as pd



#CREDENTIALS WITH SERVICE ACCOUNT GCP
credentials_path = "C:\WORK\playground-325606-PrivateKey.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

#OPEN CONNECTION TO TABLE BIGQUERY
client = bigquery.Client()
table_id = 'testingBigQuery.mahasiswa'

#INGEST DATA to TABLE
rows_to_insert = [
    {u'id_mahasiswa':'0004', u'nama':'Umms', u'jurusan':'Hubungan Internasional'},
]

errors = client.insert_rows_json(table_id, rows_to_insert)
if errors == []:
    print('New rows have been added.')
else:
    print(f'Encountered errors while inserting rows: {errors}')    
