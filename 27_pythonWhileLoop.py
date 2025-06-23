# while condition:
#     print(statement)
#     increment

# myNumber = int(input("Enter positive integer : "))

# while (myNumber ** 2 < 1000):
#     print(myNumber ** 2)
#     myNumber += 1

i = 0
while i < 5:
    print(i)
    if i == 3:
        print(f"My iteration number reach to {i}")
        i += 1
        continue
    i += 1

# normal loop  - Sab kuch bar bar run karega
# break - jaha pe break laga hai waha se loop se exit ho jayega
# continue - to loop k andar jaha continue laga hai wahi se second loop run 
# karega (without touching further code in loop)