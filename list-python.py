# list di python
# membolehkan item duplikasi

cars = ["toyota", "volvo", "tesla", "wuling"]

print (type(cars)) #tipe data
print (len(cars)) #panjang data

print(cars[0]) # memunculkan urutan ke 0 dari list

cars.append("suzuki") #menambahkan data pada list, dan data yang ditambahkan ada di paling akhir
print(cars)

cars.insert(1,"mitshubisi") #menambahkan data pada list di urutan ke 2
print(cars)

cars.remove("tesla") #menghapus berdasrkan string pada list
print(cars)

cars.pop(2) #menghapus berdasarkan urutan pada list
print(cars)

cars[2] = "dfsk" #mengupdate data berdasarkan urutan