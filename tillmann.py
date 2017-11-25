#Jugendschutzprogramm für filme
#******************************
#******************************
print("Bitte geben sie ihren Namen ein. Ich schaue auch weg... :")
print("*****************************************************************")
i = input() #variable1
print("Du heißt also " + i + ", Schöner name!")
print("wie alt bist du?")
x = int(input())  #variable2 umgewandelt in zahl
if x < 18:
	print("Du bist leider noch zu jung für den film " + i + "!")
else:
	print("Viel spaß beim Film " + i )
	print("*************************")
 	
