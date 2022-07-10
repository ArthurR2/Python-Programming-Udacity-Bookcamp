# Write your code here

# HINT: create a dictionary from flowers.txt
from numpy import full_like


def create_flowerdict(filename):
    cast_list = {}

    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower()
            flower = line.split(": ")[0].lower()
            cast_list[letter] = flower
    return cast_list

# HINT: create a function to ask for user's first and last name


def main():
    flower_d = create_flowerdict('flower.txt')
    full_name = input("Enter your First [space] Last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]
# print the desired output
    print("Unique flower name with the first letter: {}".format(
        flower_d[first_name]))


main()
