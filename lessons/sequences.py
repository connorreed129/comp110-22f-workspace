"""examples of the tuple range and sequences."""

#AN example of a tuple without type aliasing
goat: tuple[str, int] = ("MJ", 23)

#tuples are sequences so they're 0-indexed
print(goat[0])
print(goat[1])

#sequences have lengths 
print(len(goat))

#sequences are iterable with for... in loops
#meaning you can loop over them with for... in
for item in goat:
    print(item)

#tuples, unlike lists, are immutable (can't be changed)
#means cannot reassigned/ append/ pop items


#we can "invent" our own types with a type alias
Player = tuple[str, int]

#once aliased a type, can create varibles of that type
unc_poy: Player = ("Bacot", 5)

#In a strange world, where jersey number changes...
unc_poy = (unc_poy[0], unc_poy[1] + 1)



#a range is another common sequence type
zero_to_nine: range = range(0, 10, 1)

print(zero_to_nine[0])
print(zero_to_nine[9])

for i in zero_to_nine:
    print(i)



#we can habe different steps for more control
odds_to_99: range = range(1, 100, 2)
for i in odds_to_99:
    print(i)

