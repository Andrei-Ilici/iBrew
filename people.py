diction={}
done = True

def readfile():
    file = open("text.txt" , "r").read().splitlines()
    for line in file:
        (key,val) = line.split(': ')
        diction[key] = val
readfile()

while done == True:
    a = input("Please write the required key or command: ")
    if a == "write":
        try:
            write_elem = open("text.txt","a")  
            message = input("Please add a key:value to the dictionary: ")
            write_elem.write('\n' + message)
        finally:
            write_elem.close()
    if a == "stop":
        done = False
        break
    if a == "delete":
        b = input("What item do you want deleted?")
        try:
            del diction[b]
        except KeyError:
            print("Error! This is not a preexisting key! Please try a different command. ")
        print()
    if a == "update":
        ans = input("Do you want to update the key or the value? ")
        if ans == "key":
            old = input("Write the word that needs changing: ")
            new = input("Write the new word: ")
            try: 
                diction[new] = diction.pop(old)
            except KeyError:
                print ("Error! This is not a preexisting key! Please try a different command. ")
        if ans == "value":
            old = input("Write the associated key that needs changing: ")
            new = input("Write the new word: ")
            diction[old] = new
    if a == "print":
        readfile()
        for key, value in diction.items():
            print(f"{key}: {value}")
    if a!="write" and a!="print" and a!="stop" and a!="delete" and a!="update" and a not in diction.keys():
        diction[a] = input("Please add the required value: ")
        print()
        
print (diction)