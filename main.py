import random, time, function

#initialisation des variables
menu = 1
scoreList = []
scoreDeath = 0
chxmenu = None
endgame = False
mapH = 3
mapV = 3
pvm = 8 #point de vie monstre
pv = 10 #point de vie
pw = 2 #power
sh = 0 #Shield
pwm = 1 #powermonstre
shm = None
tour = 1
countDeath = 0
bgd = False
monstreCoord = function.monstercood(mapH,mapV)
characterCoord = [random.randint(1,mapH), random.randint(1,mapV)]
potion = 0
#bouclierCoord = [random.randint(1,mapH), random.randint(1,mapV)]
#epeeCoord = [random.randint(1,mapH), random.randint(1,mapV)]
#potionCoord = [random.randint(1,mapH), random.randint(1,mapV)]

#Start Program






function.clear()
#time.sleep(5)
while menu == 1:
    function.clear()
    function.menu(scoreList)
    function.clear()

    characterName = input('Quel sera le nom de notre héro: ')

    function.clear()

    print('Bienvenue jeune '+ characterName + ' tout commence ici\nTu te reveille dans une fôret.... seul\n'
    'tes souvenirs sont flou et il fait nuit...\n"Bon Chance !!!!"')

#time.sleep(5)

    function.clear()

    print('oui .... tu es seul !')

    while endgame == False:

        if countDeath == 1:
            monstreCoord = function.monstercood(mapH,mapV)
            countDeath = 0
            pvm = 8
            scoreDeath += 1


        function.clear()
        if bgd == True:
            function.background()
        
        chancePotion = random.randint(1,20)
        print('TOUR'+ str(tour))
        print(characterName + ' tu es au coordonnée ' + str(characterCoord[0]), str(characterCoord[1]))
        function.hud(pv, pw, sh, pvm)
            
        chx = int(input('Que faire :\n\n1 - Se deplacer\n2 - Rester ici\n3 - Inventaire\n\nTon choix: '))

        if chx == 1:
            if chancePotion == 1:
                function.clear()
                print('Tu as trouvé une postion')
                time.sleep(2)
                potion += 1
            characterCoord = [random.randint(1,mapH), random.randint(1,mapV)]
            function.clear()
            bgd = True
        
        elif chx == 2:
            bgd = False
        
        elif chx == 3:
            if function.hudinventaire(potion) == True and potion > 0:
                pv += 5
                potion -= 1
            bgd = False


        

        if characterCoord == monstreCoord:
            function.clear()
            monstreNV1 = function.monsternameNV1()

            #implementer la logique des niveau de monstres ici avec un random

            while countDeath !=1:
                function.clear()
                print('C O M B A T !!!!!')
                function.hud(pv, pw, sh, pvm)
                function.hudmonster(monstreNV1, pvm, pwm, shm)
                chx = int(input('Que faire :\n\n1 - Attaquer\n2 - Fuire\nTon choix ;'))
                if chx == 1:
                    touche = function.attack()
                    if touche == True:
                        pvm = pvm - pw
                    elif touche == False:
                        pv = pv - pwm
                if pvm <= 0:
                    countDeath = 1
                    function.clear()
                    print('Tu as vaincu ',monstreNV1)
                    time.sleep(2)
                    scoreDeath +=1
                    function.clear()
                    
                elif pv <= 0:
                    countDeath = 1 
                    print('GAME OVER !!!!')
                    time.sleep(2)
                    function.clear()
                    namePlayer = input('Quel est ton nom :')
                    scoreList.append((namePlayer,scoreDeath))
                    pv = 10
                    potion = 0
                    pw = 2
                    endgame = True
                        
        tour += 1 


