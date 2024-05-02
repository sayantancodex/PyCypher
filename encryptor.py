import random
import string
import time
import os 
import tokengenerator
import pymysql
from configparser import ConfigParser


def encry():
    configur = ConfigParser()
    configur.read('dbconfig.ini')
    host= configur.get("MYSQL_DB","Host")
    port = int(configur.get("MYSQL_DB","Port_number"))
    database = configur.get("MYSQL_DB","Database_name")
    user = configur.get("MYSQL_DB","Database_user")
    password = configur.get("MYSQL_DB","Database_password")

    chars = " "+string.punctuation+string.digits+string.ascii_letters

    chars = list(chars)
    key = chars.copy()

    random.shuffle(key)
    keyDB = "".join(map(str, key))

    time.sleep(3)
    f_name = tokengenerator.tokengenerator()
    print(f"YOUR TOKEN NUMBER IS {f_name}\nCOPY AND KEEP IT SAFE FOR FURTHER DECRYPTION")
    
    conn = pymysql.connect(host=host,
    user=user,
    password=password,
    database=database,
    port=port)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS cypher(
                idcode VARCHAR(256) PRIMARY KEY,
                combo VARCHAR(255)
        )
    ''')
    insert_script = 'INSERT INTO cypher(idcode, combo) VALUES(%s, %s)'
    insert_values = (f_name, keyDB)
    cur.execute(insert_script, insert_values)

    conn.commit()
    conn.close()    


    #ENCRYPT
    plain_text = input("Enter a message to encrypt: ")
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    print(f"encrypted message: {cipher_text}")