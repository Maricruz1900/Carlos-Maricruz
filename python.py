import random                       
# SuperheroType class: Defines the type of superhero with its strengths and weaknesses
class SuperheroType:
    def __init__(self, name, strengths=None, weaknesses=None):
        self.name = name
        self.strengths = [] if strengths is None else strengths  
        self.weaknesses = [] if weaknesses is None else weaknesses

# Check if the current type is strong against another type
    def is_strong_against(self, other):
        return other.name in self.weaknesses
    
# Check if the current type is weak against another type
    def is_weak_against(self, other):
        return other.name in self.strengths

# A superhero class is created, where it defines a superhero with its name, level and types
class Superhero:
    def __init__(self, name, level, types):

        self.name = name
        self.level = level
        self.types = types
        self.max_health = level * 10
        self.current_health = self.max_health
        self.is_dead = False

    def __repr__(self):
# String representation of the superhero
        type_names = "/".join([t.name for t in self.types])
        return f"{self.name} ({type_names} - Level {self.level})"

    def lose_health(self, damage):
# Reduces the current health of the superhero by the damage received
        self.current_health = max(0, self.current_health - damage)
        if self.current_health == 0:
            self.dead()

    def gain_health(self):
# Resets the superhero's current health to maximum
        self.current_health = self.max_health

    def dead(self):
# Set the superhero status to dead
        self.is_dead = True

    def revive(self):
# Revive the superhero by putting his status on live and restoring his health
        self.is_dead = False
        self.current_health = self.max_health

    def get_effectiveness(self, other_type):
# Gets the effectiveness of the superhero against a given type of superhero
        effectiveness = 1.0
        
        for type in self.types:
            for strength in type.strengths:
                if strength == other_type.name:

                    effectiveness *= 1.5
                    
            for weakness in type.weaknesses:
                if weakness == other_type.name:

                    effectiveness *= 0.8

        return effectiveness

    def attack(self, other):
       # Perform an attack on the other superhero, calculating the damage based on the effectiveness
        effectiveness = self.get_effectiveness(other.types[0])
        if len(other.types) > 1:
            effectiveness *= self.get_effectiveness(other.types[1])

        num1=int(effectiveness*self.level)
        num2=int(effectiveness*self.level/2)

        damage=random.randint(num2, num1)
        
        print(f"{self} attacks {other} and deals {damage} damage!")
        other.lose_health(damage)


def battle(superhero1, superhero2):
# Simulate a battle between the superheros
    print(f"{superhero1} vs. {superhero2}! Let the battle begin!")
    current_turn = 1
    while not superhero1.is_dead and not superhero2.is_dead:
        print(f"Round {current_turn}!")
        attacker = superhero1 if current_turn % 2 == 1 else superhero2
        defender = superhero2 if current_turn % 2 == 1 else superhero1
        attacker.attack(defender)
        current_turn += 1
    winner = superhero1 if superhero2.is_dead else superhero2
    loser = superhero1 if superhero2.is_dead is False else superhero2
    # If the superhero loses it will print a "loser" message and if he wins it will print a "winner" message
    print(f"{winner} wins!")
    print(f"{loser} lost")

    winner.gain_health()
    loser.revive()
    loser.gain_health()

# The type of superhero is defined, its fortress and debility

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

# A menu is made where you can choose the super heroes that you want them to fight
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

