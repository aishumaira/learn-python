#untuk membuat anonymus funtion/tanpa nama. Gk pake def dan kata kunci lainnya
#lambda arguments : expression

def subs(num1, num2):
    return num1 - num2

frs = subs(8,4)
print(frs)

subs_lambda = lambda num1, num2 : num1 - num2
print(subs_lambda(90,33))

#add, multiply, division
add_lambda = lambda num1, num2 : num1 + num2
print(add_lambda(67,33))

mult_lambda = lambda num1, num2 : num1 * num2
print(mult_lambda(3,33))

div_lambda = lambda num1, num2 : num1 / num2 if num2 != 0 else "Tidak bisa dibagi nol"
print(div_lambda(90,0))
print(div_lambda(90,3))

c_to_k_lambda = lambda c : c + 273.15
c_to_f_lambda = lambda c : 9/5*c + 32
c_to_r_lambda = lambda c : 4/5*c

suhu = float(input('Masukkan suhu celcius : '))
konvert = input('konvert ke ketik : F(Fahrenheit) / K(Kelvin) / R(Reamure) : ').lower() #bikin tulisan jadi huruf kecil

if konvert == 'f':
    hasil = c_to_f_lambda(suhu)
    print(f"{suhu} derajat celcius = {hasil} fahrenheit")
elif konvert == 'r':
    hasil = c_to_r_lambda(suhu)
    print(f"{suhu} derajat celcius = {hasil} reamure")
elif konvert == 'k':
    hasil = c_to_k_lambda(suhu)
    print(f"{suhu} derajat celcius = {hasil} kelvin")
else:
    print("Input tidak valid")