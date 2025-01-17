def jumlahkan(*numbers):
    #bisa nerima angka berapa aja karena pake bintang = args(tuple)
    result = 0
    for num in numbers:
        result += num
    
    return result

sum1 = jumlahkan(10,20,30,40,50,60,70)
print(sum1)

sum2 = jumlahkan(32,76,45,90)
print(sum2)

def biodata(**data):
    for key, value in data.items():
        print(key,':',value)

biodata(nama="Budi", umur=20, address="Jakarta", phone=821937)

def ratarata(*numbers):
    result = 0
    for num in numbers:
        result+=num
    total = len(numbers)
    avg = result/total

    return avg

avg1 = ratarata(87,90,89,70)
print(avg1)




