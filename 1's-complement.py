x = input("[+] Enter binary :")
list1 = []
for i in x : 
    if i == "0" : 
        list1.append("1")
    else : 
        list1.append("0")
y = "".join(list1)
print(f"[+] Result {y}")
