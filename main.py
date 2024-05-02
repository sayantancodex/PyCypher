import pyfiglet

result = pyfiglet.figlet_format("PyCypher")
print(result)
print("Made By Sayantan Patra")
print("FOLLOW ME UP ON INSTAGRAM --> https://www.instagram.com/the_eager_wolverine\nFOLLOW AND STAR MR ON GITHUB --> https://github.com/sayantancodex \n")

print("DO YOU WANT TO ENCRYPT A TEXT OR DECRYPT A CYPHER TEXT")
ch1 = int(input("[1] ENCRYPTION \n[2] DECRYPTION\n[3] EXIT\nENTER COICE --> "))

if ch1 == 1:
    import encryptor
    encryptor.encry()
    exit()

elif ch1 == 2:
    import decryptor
    decryptor.decry()
    exit()

elif ch1 == 3:
    exit()

else:
    print("INVALID INPUT! EXITING THE PROGRAM...")
    exit()


