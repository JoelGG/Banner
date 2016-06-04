def banner(name,character):
	name = ".::" + str(name) + "::."
	nameLength = len(name)
	charLength = len(character)
	overLength = nameLength/charLength
	print(character*overLength)
	print(name)
	print(character*overLength)

banner("Joel Grimmer","||")
'''github is confusing'''
