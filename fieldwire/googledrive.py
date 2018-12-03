from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaIoBaseDownload
from apiclient.http import MediaFileUpload
import sqlite3
import pandas as pd
conn = sqlite3.connect('db_fieldwire')
def gets():
    SCOPES = 'https://www.googleapis.com/auth/drive'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
        creds = tools.run_flow(flow, store)
    DRIVE = discovery.build('drive', 'v2', http=creds.authorize(Http()))
    
    #buscar = DRIVE.files().list(q="title='DataBase'",fields='nextPageToken, items(id, title)',pageToken=None).execute()
    #res = DRIVE.files().list(fields='nextPageToken, items(id, title,parents)',pageToken=None).execute()
    res = DRIVE.files().list(pageToken=None).execute()
    folder = [x for i,x in enumerate(res['items']) if (x['mimeType'] == 'application/vnd.google-apps.folder') and (len(x['parents']) > 0) and (x['parents'][0]['isRoot'] == True)]
    subfolder = [x for i,x in enumerate(res['items']) if (x['mimeType'] == 'application/vnd.google-apps.folder') and (len(x['parents']) > 0) and (x['parents'][0]['isRoot'] == False)]
    files = [x for i,x in enumerate(res['items']) if (not x['mimeType'] == 'application/vnd.google-apps.folder') and (len(x['parents']) > 0) and (x['parents'][0]['isRoot'] == False)]
    root = []
    for x in folder:
        fol = {'obj': x, 'subfolder': []}
        for y in subfolder:
            sub = {'obj': y, 'files' : []}
            if x['id'] == y['parents'][0]['id']:
               for z in files:
                   if y['id'] == z['parents'][0]['id']:
                      sub['files'].append(z) 
               fol['subfolder'].append(sub)
        root.append(fol)
    return root
#def gets(table):
#  df =pd.read_sql_query("select * from " + table + ";",conn)
#  return df
#def insert_row(table,row):
#  #c = conn.cursor()
#  #c.execute("insert into person(firstname, lastname) values (?, ?)", persons)
#  cols = ', '.join('"{}"'.format(col) for col in row.keys())
#  vals = ', '.join('"{}"'.format(col) for col in row)
#  sql = str('INSERT INTO "{0}" ({1}) VALUES ({2})'.format(table, cols, vals))
#  conn.cursor().execute(sql)
#  conn.commit()
#def cuenta():
#    cuenta.numero += 1
#    return cuenta.numero
#def update_row(table,row,idx):
#    cuenta.numero = -1
#    str1 = ', '.join('{0}="{1}"'.format(row.index[cuenta()],r) for r in row)
#    sql = str('UPDATE "{0}" SET {1} WHERE id = {2}'.format(table,str1.idx))
    #conn.cursor().execute(sql)
    #conn.commit()  