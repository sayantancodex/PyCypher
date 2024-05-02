import string
import os
import pymysql
from configparser import ConfigParser



def decry():

    print("NOTE: YOU NEED YOUR DECRYPION CODE TO DECODE")
    code = input("PLEASE ENTER YOUR DECRYPTION CODE --> ")
    

    cypher = ""
    
    configur = ConfigParser()
    configur.read('dbconfig.ini')
    host= configur.get("MYSQL_DB","Host")
    port = int(configur.get("MYSQL_DB","Port_number"))
    database = configur.get("MYSQL_DB","Database_name")
    user = configur.get("MYSQL_DB","Database_user")
    password = configur.get("MYSQL_DB","Database_password")

    conn = pymysql.connect(host=host,
    user=user,
    password=password,
    database=database,
    port=port)

    cur = conn.cursor()
    script = 'SELECT combo FROM cypher WHERE idcode='
    cur.execute(f"SELECT combo FROM cypher WHERE idcode='{code}'")
    a = cur.fetchall()    
    conn.commit()
    conn.close()

    if a == None:
        print("KEY DPESN'T EXISTS IN THE SERVER!")
        exit()
    else: 
        a = a[0]
        a = a[0]

        chars = " "+string.punctuation+string.digits+string.ascii_letters
        chars = list(chars)
        key = list(a)

        cipher_text = input("Enter a message to decrypt: ")
        plain_text = ""

        for letter in cipher_text:
            index = key.index(letter)
            plain_text += chars[index]

        print(f"DECRYPTED MESSAGE : {plain_text}")

