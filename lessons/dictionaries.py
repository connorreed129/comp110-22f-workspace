"""Demonstrations of dictionary capabilities."""


#declaring the type of dictionary
schools: dict[str, int]

#initialize to an empty dictionary
schools = dict()

#set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150


#print a dictionary literal representation
print(schools)


#Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# remove a key-value pair from a dictionary by its key
schools.pop("Duke")

#test for existence of a key
is_duke_present: bool = "Duke" in schools 
print(f"Duke is present: {is_duke_present}")

#reassign a key value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

#empty dictionary literal
schools = {} #same as dict()

#alternatively initalize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU" : 26150} 


#what happens when a key does not exist-- gets a key error that tells you which line messed up
#print(schools["UNCC"])
# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
