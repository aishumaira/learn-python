#x = membuat file baru
#r = membaca file
#w = menulis konten di file (Kalau gk ada file-nya otomatis buat file baru) (Seluruh isi file diganti sama yang baru)
#a = menambahkan konten

#open('latihan.txt', 'x')
file = open('latihan.txt', 'r')
print(file.read())

#file = open('latihan.txt', 'w')
#file.write("Selamat sore")
#file.close()

file = open('latihan.txt', 'a')
file.write("\n") #Buat enter
file.write("Salam \n")
file.close()

#with = otomatis nutup file tanpa file.close()
with open('latihan.txt', 'a') as file:
    file.write("Hai, coba dong \n")

with open('latihan.txt', 'a') as file:
    file.write("Nambah gaes, ga overwrite")

print(f'status file: {file.closed}')

file = open('latihan.txt', 'r')
print(file.readline())
print(file.readlines())

file = open('filename.txt', 'x')
file = open('filename.txt', 'r')
file = open('filename.txt', 'w')
file.write("Hai \n")
file = open('filename.txt', 'a')
file.write("Halo")