immutable_var = 1, 5.5, True, "Кортеж"
print(immutable_var)
#immutable_var [0] = 48 #Кортежи нельзя изменять, потому что они были разработаны таким образом. Кортеж хранит ссылку на список, а не сам список. Изменяемая пльтернатива кортежу - список.
mutable_list = [5.7, 142, "Список", False]
print(mutable_list)
mutable_list [0] = "Новый список"
mutable_list [2] = 6
print(mutable_list)