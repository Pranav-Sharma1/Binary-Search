print("Binary Search Algorithm. \n")

import random


userlist1 = int(input("First number of list..."))
userlist2 = int(input("Last number of list..."))
e = int(input("Enter a the number you search for..."))


def binarySearch(li, element):
	li.sort() #start by sorting list
	top = len(li) #Rather than recreating the list, these two variables are set so that we check the topsection and bottom section of the list. This is the whole list

	bottom = 0
	while top > bottom:
		print(len(li[bottom:top])) #printing the list out so we can see it when we run the program
		middle = (top + bottom)//2 # divided twice to make it an integer rather than float
		if e == li[middle]:
			return middle #Is it equal to the middle
		elif e < li[middle]:
			top = middle #Is it less than, if yes then we move the top to the middle to get bottom to top as the first half. E.g 1,2,3,4,5,6  top goes from 6 to 3 and becomes, 1,2,3. Top becomes middle.
		elif e > li[middle]:
			bottom = middle #Inverse of the above
	return -1

li = [*range(userlist1, userlist2 + 1)]#user's list range
outcome = binarySearch(li, li[random.randrange(0, len(li))])#calls binary Search and cuts down list half and then half and then half, the two parameters of li and element are assigned.
# binary seach(li - which is defined as the user's list above and, element is assigned the value of a random number from 0 to the end of the list, so we can fulfill the binary search halving.)
print("Your number: ",li[outcome])
print("Place in list: ", outcome + 1) # Create random list and select random integer to look for.We print out the length of the list each time, not the integer.
print("\n",li)


