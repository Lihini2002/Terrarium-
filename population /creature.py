from dna import DNA
import math

class Creature:
    def __init__(self, x, y, dna):
        self.x = x
        self.y =  y # creature's position in the environment
        self.dna = dna
        self.fitness = 0  # Example fitness level, can be adjusted based on your simulation needs , score of sucecess.
        self.angle = random.uniform(0, 2 * math.pi) #direction the creature is facing, in radians
        self.alive = True



class Prey(Creature):
    def __init__(self, x, y, dna):
        super().__init__(x, y, dna)
        self.weight = 5 
        self.energy = 80  # Example energy level for prey, can be adjusted based on your simulation needs
        # add metabolism metrics as scaling up 

    def move(self, food_sources, predators):
        # move towards  food sources while avoiding predators


        # Logic for prey movement
        pass

    def die(self, cause=None):
        self.alive = False
        self.energy = 0 

    def reproduce(self, partner):
        # if self.energy > reproduction_threshold and partner.energy > reproduction_threshold:
        #     self.energy -= reproduction_cost
        #     partner.energy -= reproduction_cost
            
        # call above in the place where we call it. 
        
            if not self.alive or not partner.alive:
                return None

            if self is partner:
                return None
            else: 
                child_dna = DNA.crossover(self.dna, partner.dna) 
                child_dna.mutate(mutation_rate=0.1)  # Adjust mutation rate as needed

                child = Prey(self.x, self.y, child_dna)
                return child
        
         # Crossover with partner
         # Mutate the DNA before reproduction


class Predator(Creature):
    def __init__(self, x, y, dna):
        super().__init__(x, y, dna)
        self.weight = 10  # Example weight for predators, can be adjusted based on your simulation needs
        self.energy = 120  # Example energy level for predators, can be adjusted based on your simulation needs
    
    def eat(self, prey):
        # Logic for predator to eat prey
        pass

