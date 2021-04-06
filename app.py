from suhufi import Suhufi

print("\nPengukur Suhu [Tidak] Otomatis")

j = ['°F','°C','°K']

x = 1
while x < len(j):
	for k in j:		
		print(x,'.',k)
		x += 1

u = int(input('Mau apa?\n'))

if u == 1:
	a = int(input('Masukkan suhu dalam Fahrenheit : '))
	x = Suhufi(a)
	print(a,'°F','=',x.fahrenheit(),'°C')
	print(a,'°F','=',x.fahKelvin(),'°K')

elif u == 2:
	a = int(input('Masukkan suhu dalam Celcius : '))
	x = Suhufi(a)
	print(a,'°C','=',x.celcius(),'°F')
	print(a,'°C','=',x.celKelvin(),'°K')

elif u == 3:
	a = int(input('Masukkan suhu dalam Kelvin : '))
	x = Suhufi(a)
	print(a,'°K','=',x.kelvinFah(),'°F')
	print(a,'°K','=',x.kelvinCel(),'°C')
else:
	print("Pilihan anda salah")

