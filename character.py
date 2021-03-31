class CurrentCharacter:
    def __init__(self):
       
        self.name = ''
        self.archetype = ['','']
        self.level= 0
        self.prof = 0
        self.hp = 0
        self.hitdie = 0

        self.skills = [                              
            ['Acrobatics', 0, False, 1],           #0
            ['Animal Handling', 0, False, 4],      #1
            ['Arcana', 0, False, 3],               #2
            ['Athletics', 0, False, 0],            #3
            ['Deception', 0, False, 5],            #4
            ['History', 0, False, 3],              #5
            ['Insight', 0, False, 4],              #6
            ['Intimidation', 0, False, 5],         #7
            ['Investigation', 0, False, 3],        #8
            ['Medicine', 0, False, 4],             #9
            ['Nature', 0, False, 3],               #10
            ['Perception', 0, False, 4],           #11
            ['Performance', 0, False, 5],          #12
            ['Persuasion', 0, False, 5],           #13
            ['Religion', 0, False, 3],             #14
            ['Sleight of Hand', 0, False, 1],      #15
            ['Stealth', 0, False, 1],              #16
            ['Survival', 0, False, 4]              #17
        ]

        self.stats = [
            ['Strenght', 0],                    #0
            ['Dexterity', 0],                   #1
            ['Constitution', 0],                #2
            ['Intelligence', 0],                #3
            ['Wisdom', 0],                      #4
            ['Charisma', 0]                     #5
        ]



    def setStat(self, seeker, modifier):           #Modifica los Stats
        self.stats[seeker][1] = modifier
        print(f"El stat {self.stats[seeker][0]} ahora tiene un modificador de {modifier}")



    def setProf(self):                #Establece la Proficiencia según el Nivel
        if self.level >= 1 and self.level <= 4:
            self.prof = 2
        elif self.level >= 5 and self.level <= 8:
            self.prof = 3
        elif self.level >= 9 and self.level <= 12:
            self.prof = 4
        elif self.level >= 13 and self.level <= 16:
            self.prof = 5
        elif self.level >= 17 and self.level <= 20:
            self.prof = 6



    def setHP(self):                #Establece la HP según el Nivel y la Constitucion (Stat)
        if self.level == 1:
            self.hp = self.hitdie + self.stats[2][1]
        else:
            self.hp = round(self.hitdie + (((self.hitdie/2) + 1)*(self.level - 1)) + (self.stats[2][1]*(self.level - 1)))
        print(f"Tienes un total de {self.hp} puntos de vida.")



    def setSkill(self, seeker):                   #Modifica si se sabe una Skill o no              
        if seeker == 18:
            return
        elif self.skills[seeker][2] == False:    
            self.skills[seeker][2] = True     
            print(f"Aprendiste {self.skills[seeker][0]}.")
        elif self.skills[seeker][2] == True:
            self.skills[seeker][2] = False
            print(f"Removiste {self.skills[seeker][0]}.")



    def showSkill(self):
        a = 0
        for i in range(len(self.skills)): 
            a += 1
            if a == 3 or i == 17:
                a = 0
                b = "\n"
            elif len(str(i) + ". " + self.skills[i][0]) > 15:
                b = "\t"
            else:
                b = "\t\t"
            print(i, end = ". ")
            print(self.skills[i][0], end = f"{b}")



    def showAllSkill(self):          #Actualiza la lista de Skills sumándole Stats, además de Proficiencia si se sabe el Skill
        for i in range(len(self.skills)):   
            self.skills[i][1] += self.stats[self.skills[i][3]][1]
        
            if self.skills[i][2] == False:
                learnt = "⦾"
            elif self.skills[i][2] == True:
                learnt= "⦿"
                self.skills[i][1] += self.prof
            
            print(f"{learnt}  {self.skills[i][0]}  {self.skills[i][1]} ") 