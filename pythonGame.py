
class SuperheroType:
    def __init__(self, name, strengths=None, weaknesses=None):

     
        self.name = name
        self.strengths = [] if strengths is None else strengths  
        self.weaknesses = [] if weaknesses is None else weaknesses

    def is_strong_against(self, other):

        return other.name in self.weaknesses

    def is_weak_against(self, other):

        return other.name in self.strengths

#The type of superhero is defined, its fortress and debility

arachnid_type = SuperheroType ("Arachnid", strengths=["Magic" , "Fast"], weaknesses=["Thunder" , "Bat"])
thunder__type = SuperheroType ("Thunder", strengths=["Arachnid" , "Bat"], weaknesses=["Fast" , "Magic"])
fast_type = SuperheroType ("Fast", strengths=["Thunder"], weaknesses=["Bat" , "Arachnid"])
bat_type = SuperheroType ("Bat", strengths=["Magic"], weaknesses=["Arachnid" , "Thunder"])
magic_type = SuperheroType ("Magic", strengths=["Fast" , "Thunder"], weaknesses=["Bat" , "Arachnid"])


# Create the superheros with their level

spiderman = Superhero("Spiderman", 10, [arachnid_type])
thor = Superhero("Thor", 10, [thunder__type])
flash = Superhero("Flash", 10, [fast_type])
batman = Superhero("Batman", 10, [bat_type])
strange = Superhero("Dr. Strange", 10, [magic_type])

# Simulate battles between the superheros
while True:
    print ("1-Spiderman")
    print ("2-Thor")
    print ("3-Flash")
    print ("4-Batman")
    print ("5-Dr. Strange")
    s1=int(input("Select the first superhero: "))
    s2=int(input("Select the second superhero: "))
    if s1==1: 
        super1=spiderman
    elif s1==2:
        super1=thor
    elif s1==3:
        super1=flash
    elif s1==4:
        super1=batman
    elif s1==5:
        super1=strange

    if s2==1: 
        super2=spiderman
    elif s2==2:
        super2=thor
    elif s2==3:
        super2=flash
    elif s2==4:
        super2=batman
    elif s2==5:
        super2=strange
    battle(super1, super2)

