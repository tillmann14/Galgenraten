def durchschnitt():
	i = 0
	summe = 0
	u = input()
	while u != "":
		print("gut")

		i = i + 1
		summe = summe + int(u)
		u = input()
	print(summe/i)		
	return summe/i

print ((durchschnitt() + durchschnitt())/2)
