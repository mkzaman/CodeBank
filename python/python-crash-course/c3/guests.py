guests = ['kareema', 'karim', 'shahida']

print(f"Hello {guests[0]}, please come to my party!")
print(f"Hello {guests[1]}, please come to my party!")
print(f"Hello {guests[2]}, please come to my party!")

print(f"{guests[1]} can't come to the party :( :( ))")

guests[1] = 'abdullah'

print(f"Hello {guests[0]}, please come to my party!")
print(f"Hello {guests[1]}, please come to my party!")
print(f"Hello {guests[2]}, please come to my party!")

print("Got a bigger table")

guests.insert(0, 'sweety')
guests.insert(1, 'shovon')
guests.append('rasel')

print(f"Hello {guests[0]}, please come to my party!")
print(f"Hello {guests[1]}, please come to my party!")
print(f"Hello {guests[2]}, please come to my party!")
print(f"Hello {guests[3]}, please come to my party!")
print(f"Hello {guests[4]}, please come to my party!")
print(f"Hello {guests[5]}, please come to my party!")

print("Sorry, I can invite only two people :( :( ))")

guests.pop()
guests.pop()
guests.pop()
guests.pop()

print(f"Hello {guests[0]}, please come to my party!")
print(f"Hello {guests[1]}, please come to my party!")

print("party's over")

del guests[0]
del guests[0]

print("WoW! Such empty")

print(guests)
