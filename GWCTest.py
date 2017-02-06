#name=input("Whose birthday is it?")
#print("Happy birthday, "+name+"!")
#age=input("How old are you now?")
#print("Wow! "+age+" years old!")

print("You just woke up and you are running late for school!")
said_get_ready = False
while not said_get_ready:
	user_input = input("You have to get ready for school. What will you do? ")
	if user_input == "get ready for school":
		said_get_ready = True
		print("You better hurry!")
	elif user_input == "get ready":
		print("Be more specific!")
		said_get_ready = False
	else:
		said_get_ready = False
		print("You're wasting time!")