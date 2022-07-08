cast = (("Barney", 72), ("Robin", 68), ("Ted", 72),
        ("Lily", 66), ("Marshall", 76))

# define names and heights here
names = tuple([i for i, j in cast])

heights = tuple([j for i, j in cast])

print(names)
print(heights)
