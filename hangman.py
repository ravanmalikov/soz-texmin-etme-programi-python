name=input("Your name: ")

print(f"Salam {name } hangman oynamagin vaxtidir.haaaaa")

mystring="melikov"

your_point=10

mylist=[i for i in mystring]

find_list=list()

while your_point >0:

	for element in mystring:
		if element in find_list:

			print(element)
		else:
			print("-")	
	
	myletter=input("Herf texmin et: ")

	if myletter in mylist:

		find_list.append(myletter)

		mylist.remove(myletter)

		print(f"Duzdur: Sozun terkibinde {myletter} herfi var.")

		if mylist==list():
			print("You won!!!!")
			break
	else:
		print("Sehvdir")
		your_point -=1
		print(f"Senin {your_point} canin qaldi.")

if your_point == 0:	

	print("You died!!!!!")			



