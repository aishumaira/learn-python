#object oriented programming
#membuat class
class Animal: #Disarankan nama classnya depannya huruf besar
    name = "" #variabel (Tapi di class disebut class propeties. Ciri yang dimiliki suatu objek)
    color = ""
    voice = ""

    #class constructor yang dijalanin pertama kali setelah dibuat objek
    def __init__(self, animal_name, animal_color):
        self.name = animal_name
        self.color = animal_color
    
    #class method (Function dalam class) =>Aktivitas yg bisa dilakukan oleh class
    def makeSound(self, sound): #Harus ada self
        print(f"{self.name}, with color {self.color}, is making sound {sound}")

    def eat(self, food):
        print(self.name, "is eating", food)

#membuat object
cat = Animal("Muffy", "Black and white")
panda = Animal("Poppy", "Red and white")

print("---------")

print(type(cat))
print(type(panda))

cat.name = "Muffy"
cat.color = "Black and White"
print(cat.name)
cat.makeSound("meong")
cat.eat("fish")

panda.name = "Poppy"
panda.color = "Red and White"


