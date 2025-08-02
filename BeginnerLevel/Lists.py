#3.List

# Initial Justice League list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)

# 1. Calculate the number of members
print("\n Number of members:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\n After adding Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to the beginning (make her the leader)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\n Wonder Woman as leader:", justice_league)

# 4. Separate Aquaman and Flash by inserting Superman or Green Lantern
justice_league.remove("Superman")  
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Superman")  
print("\n Superman placed between Aquaman and Flash:", justice_league)

# 5. Crisis - Replace with new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\n New Justice League team after crisis:", justice_league)

# 6. Sort alphabetically
justice_league.sort()
print("\n Sorted Justice League (new leader at index 0):", justice_league)
print("New leader is:", justice_league[0])
