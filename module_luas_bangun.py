import math

#Akar Kuadrat
number = int(input("Masukkan Bilangan: "))
sqrt_result = math.sqrt(number)
print(f"Akar kuadrat dari {number} adalah: {sqrt_result}")

#Bilangan berpangkat
base = int(input("Masukkan Bilangan: "))
eksponen = int(input("Masukkan Bilangan: "))
power_result = math.pow(base, eksponen)
print(f"{base} pangkat {eksponen} adalah: {power_result}")

#Menghitung Sin dan Cos
angle = int(input("Masukkan Bilangan: "))
sin_result = math.sin(angle)
print(f"Sin dari 30 derajat adalah: {sin_result}")
cos_result = math.cos(angle)
print(f"Cos dari 30 derajat adalah: {cos_result}")

#Menghitung Faktorial
fact_number = int(input("Masukkan Bilangan: "))
fact_result = math.factorial(fact_number)
print(f"Faktorial dari {fact_number} adalah: {fact_result}")