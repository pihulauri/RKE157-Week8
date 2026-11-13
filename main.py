from fight import calculate_hit
from read_from_file import read_data

villain = read_data(r"data/villains.txt")
hero = read_data(r"data/heroes.txt")

hero_weapon = read_data("data/weapons.txt")
villain_weapon = read_data("data/weapons.txt")

# print(villain)
# print(hero)

hero_hit = calculate_hit(hero, hero_weapon)
villain_hit = calculate_hit(villain, villain_weapon)

print(f"{hero} uses {hero_weapon} and hits with power {hero_hit}.")
print(f"{villain} uses {villain_weapon} and hits with power {villain_hit}.")

if hero_hit > villain_hit:
    print(f"{hero} saves the day")
elif villain_hit > hero_hit:
    print (f"{villain} and the Drk side wins!")
else:
    print("it is a tie!")
