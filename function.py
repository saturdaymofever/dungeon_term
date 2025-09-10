import random, os, time

def attack():
    touche = False
    hit = random.randint(1,6)
    print(hit)
    if hit >= 4:
        touche = True
        print('touche')
    else:
        touche = False
        print('pas touche')
    return(touche)

def score(scoreList):
    for score in scoreList:
        print('*******************')
        print(score[0], 'a marqué', score[1], 'points')
    input("Appuie sur Entrée pour continuer...")
    clear()
    menu(scoreList)


def menu(scoreList):
    chxmenu = 5
    print("++++++++++++++++++++++++++")
    print("+ Dungeaon Terminal V0.1 +")
    print("++++++++++++++++++++++++++\n")
    print('1-NewGame\n2-Score\n3-Regle\n4-Quit')
    print('')

    while chxmenu != 1:

        chxmenu = int(input('Choix : '))

        if chxmenu == 2:
            score(scoreList)
        elif chxmenu == 3:
            print('Mes regles')
        elif chxmenu == 4:
            break

def hud(pv, pw, sh, pvm):
    print('********************')
    print('    STAT')
    print('********************')
    print(' Point de vie :', pv)
    print(' Puissance    :',pw)
    print(' Bouclier     :',sh)
    print('********************')


def hudmonster(monstre, pvm, pwm, shm):
    print('********************')
    print(       monstre)
    print('********************')
    print(' Point de vie :', pvm)
    print(' Puissance    :',pwm)
    print(' Bouclier     :',shm)
    print('********************')

def hudinventaire(potion):
    chx = False
    choix = None
    print('********************')
    print(' Potion de vie (+5) :', potion)
    print('********************')
    chx = str(input('Utiliser ? o/n :'))
    if chx == 'o':
        choix = True
    else:
        choix = False
    os.system('clear')
    return(choix)


def clear():
    os.system('clear')

def background():
    descriptions = [
        "Forêt dense – Les troncs serrés comme des remparts bloquent ta vue, seuls quelques rayons de lumière se faufilent.",
        "Clairière lumineuse – Le soleil chauffe l’herbe humide, des papillons virevoltent entre les fleurs sauvages.",
        "Sentier boueux – Tes pas s’enfoncent dans la terre gorgée d’eau, chaque craquement de branche t’inquiète.",
        "Sous-bois moussu – Le sol est doux, recouvert de mousse, et l’air porte une odeur d’humus et de champignons.",
        "Ruisseau caché – Le clapotis de l’eau t’attire vers un petit cours d’eau serpentant entre les pierres moussues.",
        "Forêt embrumée – Un épais brouillard rend chaque silhouette floue, et ton souffle se mélange à la brume.",
        "Arbres tordus – Leurs branches tordues ressemblent à des bras squelettiques qui s’étirent vers toi.",
        "Chêne gigantesque – Un arbre ancien domine les lieux, son tronc si large qu’il faudrait dix hommes pour l’encercler.",
        "Sol couvert de feuilles mortes – Tes pas s’accompagnent d’un bruit sec, comme un feu qui crépite sous tes pieds.",
        "Éboulis forestier – Des roches tombées bloquent partiellement le passage, entrelacées de racines épaisses.",
        "Forêt silencieuse – Le silence est total, pas un oiseau, pas un insecte, comme si la nature retenait son souffle.",
        "Bordure d’un marécage – La terre devient molle, l’eau stagnante attire des nuées de moustiques.",
        "Tronc creux – Un immense tronc effondré sert d’abri à des champignons et de cachette pour de petites bêtes.",
        "Parterre de fougères – Les hautes feuilles vertes forment un tapis épais qui cache presque le sol.",
        "Racines enchevêtrées – Le chemin est semé d’embûches, les racines forment un piège naturel sous tes pieds.",
        "Forêt en pente – Le terrain s’élève brusquement, et les arbres semblent grimper avec toi vers la lumière.",
        "Rocher couvert de mousse – Un énorme bloc de pierre émerge du sol, glissant au toucher et constellé de lichens.",
        "Sentier effacé – Le chemin semble disparaître, avalé par la végétation qui se referme autour de toi.",
        "Forêt crépusculaire – Le ciel rougit entre les branches, et l’ombre s’étend à une vitesse inquiétante.",
        "Arbres aux écorces griffées – Des marques profondes rappellent le passage récent d’un animal sauvage."
    ]
    print(random.choice(descriptions))

def monsternameNV1():
    monstres = [
        "Loup affamé",
        "Ours brun",
        "Sanglier enragé",
        "Serpent venimeux",
        "Araignée géante",
        "Corbeau aux yeux rouges",
        "Esprit de la forêt",
        "Goule rampante",
        "Gobelin rôdeur",
        "Troll des bois",
        "Dryade corrompue",
        "Ent sombre",
        "Spectre brumeux",
    ]
    return(random.choice(monstres))

def monsternameNV2():
    monstres = [
        "Chauve-souris géante",
        "Guêpe monstrueuse",
        "Rat géant",
        "Loup-garou solitaire",
        "Squelette oublié",
        "Chien sauvage",
        "Harpie hurlante"
    ]
    return(random.choice(monstres))

def monstercood(mapH,mapV):
    x = random.randint(1,mapH)
    y = random.randint(1,mapV)
    return([x,y])

