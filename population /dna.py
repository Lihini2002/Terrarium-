
import random


"""
DNA class for representing the genetic characteristics of creatures.
I think this module can be rewritten to incorporate different ranges for differnt preys and predators. in a scalable way
what would predators and preys have differntly among their genes? 
"""


class DNA:
    def __init__(self,speed, size, vision_range, turning_speed):
        self.speed = speed
        self.size = size
        self.vision_range = vision_range
        self.turning_speed = turning_speed

    def randomize(self):
        # Randomly assign values to the DNA attributes
        self.speed = random.uniform(1, 5)  # Example range for speed
        self.size = random.uniform(0.5, 2.0)   # Example range for size
        self.vision_range = random.uniform(50, 150.0)  # Example range for vision range
        self.turning_speed = random.uniform(0.05, 0.2)  # Example range for turning speed
        self.reproduction_threshold = random.uniform(40, 120)  # Example range for reproduction threshold``
        self.agression = 0 #edit these to be variable later. 
        self.fear = 0

    # play with the mutation rate to see how it affects the population
    # let the user play with it later? 
    def mutate(self, mutation_rate=0.1):
        # Randomly mutate the DNA attributes based on the mutation rate
        if random.random() < mutation_rate:
            self.speed += random.uniform(-0.5, 0.5)
        if random.random() < mutation_rate:
            self.size += random.uniform(-0.1, 0.1)
        if random.random() < mutation_rate:
            self.vision_range += random.uniform(-10, 10)
        if random.random() < mutation_rate:
            self.turning_speed += random.uniform(-0.01, 0.01)

        # Clamp values to ensure they stay within reasonable boundaries
        self.speed = max(1.0, min(self.speed, 5.0))
        self.size = max(0.5, min(self.size, 2.0))
        self.vision_range = max(50.0, min(self.vision_range, 150.0))
        self.turning_speed = max(0.05, min(self.turning_speed, 0.2))
   
    @staticmethod
    def crossover(dna1, dna2):
        # Perform crossover between two DNA instances to create a new DNA instance
        new_speed = (dna1.speed + dna2.speed) / 2
        new_size = (dna1.size + dna2.size) / 2
        new_vision_range = (dna1.vision_range + dna2.vision_range) / 2
        new_turning_speed = (dna1.turning_speed + dna2.turning_speed) / 2

        return DNA(new_speed, new_size, new_vision_range, new_turning_speed)    
    

# class preyDNA(DNA):
#     def __init__(self, speed, size, vision_range, turning_speed):
#         super().__init__(speed, size, vision_range, turning_speed)
#         # Additional attributes specific to prey can be added here

#         self.fear = random.uniform(0.0, 1.0)  # Example fear level for prey, can be adjusted based on your simulation needs
#         self.reproduction_threshold = random.uniform(40, 120)  # Example reproduction threshold for prey, can be adjusted based on your simulation needs
#         self.fertility = random.uniform(0.5, 1.5)  # Example fertility level for prey, can be adjusted based on your simulation needs




# class predatorDNA(DNA):
#     def __init__(self, speed, size, vision_range, turning_speed):
#         super().__init__(speed, size, vision_range, turning_speed)
#         # Additional attributes specific to predators can be added here

#         self.aggressiveness = random.uniform(0.0, 1.0)  # Example aggressiveness level for predators, can be adjusted based on your simulation needs
#         self.hunting_success_rate = random.uniform(0.5, 1.0)  # Example hunting success rate for predators, can be adjusted based on your simulation needs
#         self.reproduction_threshold = random.uniform(60, 150)  # Example reproduction threshold for predators, can be adjusted based on your simulation needs