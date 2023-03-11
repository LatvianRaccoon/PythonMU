from random import randrange


class Pet:
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']

    def __init__(self, name='Kitty'):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "Happy"
        else:
            return "Bored"

    def __str__(self):
        state = "    I'm {}. ".format(self.name)
        state += "   I feel {}. ".format(self.mood())
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)


class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def feed(self):
        Pet.feed(self)
        print("Arf! Thanks!")


d1 = Dog("Astro")

d1.feed()


class Bird(Pet):
    sounds = ["chirp"]

    def __init__(self, name="Kitty", chirp_number=2):
        Pet.__init__(self, name)
        self.chirp_number = chirp_number

    def hi(self):
        for i in range(self.chirp_number):
            print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()


b1 = Bird('tweety', 5)
b1.teach("Polly wanna cracker")
b1.hi()
