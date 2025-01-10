def hello_world():
    print("Hello World")
    print("Welcome")
#1hello_world => gk boleh
#def = definition
#Kalau diakhiri dengan :, namanya blokade. Harus ada yg masuk sekali take, jadi si print punya def
hello_world()
hello_world()
hello_world()

def hello_name(name="Friend"):
    print("Hello", name + "!")
#name = parameter

hello_name("Salma")
hello_name("Yaya")
hello_name("Yuki")
#hello_name() => jadi error karena name-nya kosong
hello_name()#gk error karena ditambahin devolt value = friend

def greeting(name, age=0):
    print(f"Hello {name}! You are {age} years old.")
#f string

greeting("Salsa", 20)
greeting("Caca", 26)
greeting("Yuki")

def add(num1, num2):
    hasil = num1 + num2
    return(hasil)
#return gk langsung nampilin hasil, tapi disimpen dulu
addition = add(10,20)
dikali_10 = addition * 10
print(dikali_10)

def sub(num1, num2):
    hasil = num1 - num2
    return(hasil)
subtraction = sub(20,10)
print(subtraction)

def kali(num1, num2):
    hasil = num1 * num2
    return(hasil)
perkalian = kali(20,10)
print(perkalian)

def bagi(num1, num2):
    if num2 == 0:
        return "Tidak bisa dibagi 0"
    else:
        hasil = num1/num2
        return hasil
bagi1 = bagi(10,2)
print(bagi1)
bagi2 = bagi(20,0)
print(bagi2)

def full_name(fname, lname):
    print(f"Hello {fname} {lname}!")

full_name("Salma", "Nur") #Positional argument
full_name(lname="Nur", fname="Salma") #Keyword argument

def bmi(bb, tb):
    if tb == 0:
        return "Tinggi badan tidak boleh 0"
    else:
        bmi = bb/(tb*tb)
    
        if bmi < 18.5:
            return("Kekurangan berat badan")
        elif bmi >= 18.5 and bmi < 24.9:
            return("Normal(ideal)")
        elif bmi >= 25.0 and bmi < 29.9:
            return("Kelebihan berat badan")
        else:
            return("Kegemukan(Obesitas)")

bb = int(input("Masukkan berat badan anda "))
tb = float(input("Masukkan tinggi badan anda dalam ukuran meter "))
#int = bilangan bulat

data = bmi(bb,tb)
print(data)


