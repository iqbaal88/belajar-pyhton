# Python - Tuple

# Buatlah sebuah variable 'cars' dan isi dengan list nama nama buah berikut ini
# honda, toyota, suzuki, wuling
cars = ("honda", "toyota", "suzuki", "wuling")
print(cars)


# print hanya merk mobil 'wuling'
print(cars[3])


# tambahkan nama merk mobil baru yaitu 'daihatsu' ke dalam list 'cars'
car_list = list(cars) # rubah tuple ke dalam list
car_list.append("daihatsu") # tambahkan item
cars = tuple(car_list) # rubah kembali ke dalam tuple
print(cars)


# hapus nama merk mobil 'toyota' dari dalam list
car_list = list(cars)
car_list.remove("toyota")
cars = tuple(car_list)
print(cars)

# ubah nama merk mobil 'suzuki' menjadi 'mitsubishi'
car_list = list(cars)
car_list[2] = "mitshubishi"
cars = tuple(car_list)
print(cars)
