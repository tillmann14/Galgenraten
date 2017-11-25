import random
print("Das etwas andere Galgenraten mit dem Thema :,,Eigenbaukombinat''")
print("**********************************************************")
wörter = ["laser","tastatur","spende","maus","galgenraten","eigenbaukombinat","computer","scratch","python","junghacker"]
       #0       #1        #2      #3     #4             #5                 #6         #7        #8       #9(len(wörter))
def galgenraten(wort):
	
	def anzeigen():
		text = ""
		for buchstabe in wort:
			if buchstabe in erraten:
				text = text + buchstabe
			else:
				text = text + "_"
		return text
				
	fehler = 0
	gewonnen = False
	erraten = list()
	
	while fehler <= 5 and gewonnen == False:
		buchstabe = input()
		if buchstabe in wort:
			if (buchstabe in erraten) == False:
				for i in range(0,wort.count(buchstabe)):
					erraten.append(buchstabe)		
		else:
			fehler = fehler + 1
		print(anzeigen())
		if len(erraten) == len(wort):
			gewonnen =True
			print("Du hast es erraten")

		
zufall =random.randrange (0,len(wörter))
                               #letzte Zahl

galgenraten(wörter[zufall])

