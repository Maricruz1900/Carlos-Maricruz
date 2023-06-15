arachnid_type = SuperheroType ("Arachnid", strengths=["Magic" , "Fast"], weaknesses=["Thunder" , "Bat"])
thunder__type = SuperheroType ("Thunder", strengths=["Arachnid" , "Bat"], weaknesses=["Fast" , "Magic"])
fast_type = SuperheroType ("Fast", strengths=["Thunder"], weaknesses=["Bat" , "Arachnid"])
bat_type = SuperheroType ("Bat", strengths=["Magic"], weaknesses=["Arachnid" , "Thunder"])
magic_type = SuperheroType ("Magic", strengths=["Fast" , "Thunder"], weaknesses=["Bat" , "Arachnid"])


spiderman = Superhero("Spiderman", 10, [arachnid_type])
thor = Superhero("Thor", 10, [thunder__type])
flash = Superhero("Flash", 10, [fast_type])
batman = Superhero("Batman", 10, [bat_type])
strange = Superhero("Dr. Strange", 10, [magic_type])

battle(super1, super2)