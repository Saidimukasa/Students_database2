print("-----Program for Student Information at Uganda Christian University-----")

Dict_storage = dict()

number_of_students = int(input('How many student record you want to store?? '))

# Add student information
# to the dictionary
for i in range(0,number_of_students):
	x, y = input("Enter the complete name (First and last name) of student: ").split()
	contact = input("Enter contact number: ")
	marks = input('Enter Marks: ')
	Dict_storage[x, y] = (contact, marks)
	
# define a function for shorting
# names based on first name
def sort():
	list_storage = list()
	# fetch key and value using
	# items() method
	for sname,details in Dict_storage.items():
	
		# store key parts as an tuple
		tuple_storage = (sname[0],sname[1])
		
		# add tuple to the list
		list_storage.append(tuple_storage)
		
	# sort the final list of tuples
	list_storage = sorted(list_storage)
	for i in list_storage:
	
		# print first name and second name
		print(i[0],i[1])
	return

# define a function for
# finding the minimum marks
# in stored data
def minmarks():
	list_storage = list()
	# fetch key and value using
	# items() methods
	for sname,details in Dict_storage.items():
		# add details second element
		# (marks) to the list
		list_storage.append(details[1])
	
	# sort the list elemnts
	list_storage = sorted(ls)
	print("Minimum marks: ", min(ls))
	
	return

# define a function for searching
# student contact number
def searchdetail(fname):
	list_storage = list()
	
	for sname,details in Dict_storage.items():
	
		tup=(sname,details)
		list_storage.append(tup)
		
	for i in list_storage:
		if i[0][0] == fname:
			print(i[1][0])
	return

# define a function for
# asking the options
def option():

	choice = int(input('Enter the operation detail: \n \
	1: Sorting using first name \n \
	2: Finding Minimum marks \n \
	3: Search contact number using first name: \n \
	4: Exit\n \
	Option: '))
	
	if choice == 1:
		# function call
		sort()
		choice = input('Want to perform some other operation??? Y or N: ')
		inp = input()
		if choice == 'Y':
			option()
			
		# exit function call
		exit()
		
	elif choice == 2:
		minmarks()
		choice = input('Want to perform some other operation??? Y or N: ')
		
		choice = input()
		if inp == 'Y':
			option()
		exit()
		
	elif choice == 3:
		first = input('Enter first name of student: ')
		searchdetail(first)
		
		choice = input('Want to perform some other operation??? Y or N: ')
		
		if choice == 'Y':
			option()
			
		exit()
	else:
		print('Thanks for executing me!!!!')
		exit()
		
option()
