from character import *
from editor import checkValue, waitCalculation

char = CurrentCharacter()

print("Ingresa el nombre de tu personaje: ", end="")
char.name = input()


print("Ingresa el nivel de tu personaje: ", end="")
char.level = checkValue(0)
char.setProf()


print("Ingresa la clase de tu personaje: ", end="")
char.archetype[0] = input()


print("¿Tiene arquetipo? Ingresa Enter si no es el caso: ", end="")
char.archetype[1] = input()


for i in range(len(char.stats)):
    print(f"\nIngresa el modificador del atributo {char.stats[i][0]}: ", end="") 
    modifier = checkValue(1)
    char.setStat(i, modifier)   


print("\nIngresa el valor de tu hit die (6, 8, 10, 12): ", end="")
char.hitdie = checkValue(2)
char.setHP() 


print("\nEscoge una habilidad para aprender ingresando un valor numérico.\nIngresa '18' para terminar.")
char.showSkill()
choice = ''
while choice != 18:
    choice = checkValue(3)
    char.setSkill(choice) 
del choice


waitCalculation()


print("************FICHA************")
print(f"{char.name}, {char.archetype[0]} {char.archetype[1]}")
print("Tu nivel es: ", char.level)
print(f"Tu hit die es d{char.hitdie} y tienes {char.hp} puntos de vida máxima.")
print("Tu modificador de proficiencia es: ", char.prof)
print("************STATS************")
for i in range(len(char.stats)):
    print(char.stats[i])
print("***********PROFS*************")
char.showAllSkill()