
grp = int(input("Enter how many contacts you want to enter: "))
group = {}

for x in range (1, grp + 1, 1 ):
    name = input("Enter a name: ").lower()
    number = int(input("Enter their contact number: "))
    group[name] = number
    group.update({name:number})
    
search = input("\nEnter a name to search: ").lower()

if search in group:
    print(f"number: {group[search]}")
else:
    print("does not exist")

print(group)
 
