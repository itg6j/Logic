x = input("[+] Enter binary :")
list1 = []
for i in x : 
    if i == "0" : 
        list1.append("1")
    else : 
        list1.append("0")
y = "".join(list1)
two = int(y,2) + 1
z = bin(two)[2:].zfill(len(x))
print(f"[+] 1's complement : {y}")
print(f"[+] 2's complement : {z}")
