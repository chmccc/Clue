from random import randint
import random
import time

''' LAST UPDATE:
move comp_knows_X functions to comp_take_turn so that cDeck will update with KLR codes
'''

#drop player in a random room
playerLocation = randint(13,22)
cLoc = randint(13,22)
bCompTrickingForChar = 0
bCompTrickingForWeap = 0
bCompTrickingForRoom = 0

#just a counter for how many turns it takes the player to win
turns = 0

playerDeck = {
    1 : ["(1)", "Mr. Green", "???", " "],
    2 : ["(2)", "Col. Mustard", "???", " "],
    3 : ["(3)", "Mrs. Peacock", "???", " "],
    4 : ["(4)", "Prof. Plum", "???", " "],
    5 : ["(5)", "Miss Scarlet", "???", " "],
    6 : ["(6)", "Mrs. White", "???", " "],
    7 : ["(7)", "Candlestick", "???", " "],
    8 : ["(8)", "Knife", "???", " "],
    9 : ["(9)", "Lead Pipe", "???", " "],
    10 : ["(10)", "Revolver", "???", " "],
    11 : ["(11)", "Rope", "???", " "],
    12 : ["(12)", "Wrench", "???", " "],
    13 : ["(13)", "Hall", "???", " "],
    14 : ["(14)", "Lounge", "???", " "],
    15 : ["(15)", "Dining Room", "???", " "],
    16 : ["(16)", "Kitchen", "???", " "],
    17 : ["(17)", "Ball Room", "???", " "],
    18 : ["(18)", "Conservatory", "???", " "],
    19 : ["(19)", "Billiard Room", "???", " "],
    20 : ["(20)", "Library", "???", " "],
    21 : ["(21)", "Study", "???", " "]
}

# this is mostly useless except when dealing the AI's hand and will be removed
cheatDeck = {
    1 : ["(1)", "Mr. Green", "???", "X"],
    2 : ["(2)", "Col. Mustard", "???", "X"],
    3 : ["(3)", "Mrs. Peacock", "???", "X"],
    4 : ["(4)", "Prof. Plum", "???", "X"],
    5 : ["(5)", "Miss Scarlet", "???", "X"],
    6 : ["(6)", "Mrs. White", "???", "X"],
    7 : ["(7)", "Candlestick", "???", "X"],
    8 : ["(8)", "Knife", "???", "X"],
    9 : ["(9)", "Lead Pipe", "???", "X"],
    10 : ["(10)", "Revolver", "???", "X"],
    11 : ["(11)", "Rope", "???", "X"],
    12 : ["(12)", "Wrench", "???", "X"],
    13 : ["(13)", "Hall", "???", "X"],
    14 : ["(14)", "Lounge", "???", "X"],
    15 : ["(15)", "Dining Room", "???", "X"],
    16 : ["(16)", "Kitchen", "???", "X"],
    17 : ["(17)", "Ball Room", "???", "X"],
    18 : ["(18)", "Conservatory", "???", "X"],
    19 : ["(19)", "Billiard Room", "???", "X"],
    20 : ["(20)", "Library", "???", "X"],
    21 : ["(21)", "Study", "???", "X"]
}

# AI's deck
cDeck = {
    1 : ["(1)", "Mr. Green", "???", "X"],
    2 : ["(2)", "Col. Mustard", "???", "X"],
    3 : ["(3)", "Mrs. Peacock", "???", "X"],
    4 : ["(4)", "Prof. Plum", "???", "X"],
    5 : ["(5)", "Miss Scarlet", "???", "X"],
    6 : ["(6)", "Mrs. White", "???", "X"],
    7 : ["(7)", "Candlestick", "???", "X"],
    8 : ["(8)", "Knife", "???", "X"],
    9 : ["(9)", "Lead Pipe", "???", "X"],
    10 : ["(10)", "Revolver", "???", "X"],
    11 : ["(11)", "Rope", "???", "X"],
    12 : ["(12)", "Wrench", "???", "X"],
    13 : ["(13)", "Hall", "???", "X"],
    14 : ["(14)", "Lounge", "???", "X"],
    15 : ["(15)", "Dining Room", "???", "X"],
    16 : ["(16)", "Kitchen", "???", "X"],
    17 : ["(17)", "Ball Room", "???", "X"],
    18 : ["(18)", "Conservatory", "???", "X"],
    19 : ["(19)", "Billiard Room", "???", "X"],
    20 : ["(20)", "Library", "???", "X"],
    21 : ["(21)", "Study", "???", "X"]
}

# function junction baby

# print a deck, use dictionaries above as argument when calling
def print_card(deck):
	for i in range(1,22):
		if i == 1:
			print "CHARACTERS"
		print deck[i][0] + " " + deck[i][1] + ": " + deck[i][2] + "  " + deck[i][3]
		if i == 6:
			print "WEAPONS"
		if i == 12:
			print "ROOMS"

			
# commit the murder!
kChar = randint(1,6)
kWeap = randint(7,12)
kRoom = randint(13,22)

'''
##### DEBUG MURDER
kChar = 1
kWeap = 7
kRoom = 13
'''

# list used to avoid double-dealing
cardsDealt = []
cardsDealt.append(kChar)
cardsDealt.append(kWeap)
cardsDealt.append(kRoom)

# only useful for debug
cheatDeck[kChar][2] = "Killer"
cheatDeck[kWeap][2] = "Killer"
cheatDeck[kRoom][2] = "Killer"
    
# do not fuck with this without setting up program for more than 2 players...
handsize = 9


# deal cards to the player, checks against cardsDealt, making sure not to deal the killer cards
def deal_player_hand(handsize):
    for i in range(1, (handsize + 1)):
        randCard = randint(1,21)
        while randCard in cardsDealt:
            randCard = randint(1,21)
        cardsDealt.append(randCard)
        playerDeck[randCard][2] = "In hand"
        cheatDeck[randCard][2] = "Dealt to Player"
'''
# ***do not call before dealing the player hand!!*** otherwise computer gets all the cards
'''
def deal_comp_hand():
    for key in cheatDeck:
        if cheatDeck[key][2] == "???":
            cheatDeck[key][2] = "Dealt to Computer"
            cDeck[key][2] = "H"
'''
###### DEBUG DECK FOR COMPUTER          
def deal_comp_debug_hand():
	global cDeck
	cDeck = {
	1 : ["(1)", "Mr. Green", "???", "X"],
    2 : ["(2)", "Col. Mustard", "???", "X"],
    3 : ["(3)", "Mrs. Peacock", "???", "X"],
    4 : ["(4)", "Prof. Plum", "H", "X"],
    5 : ["(5)", "Miss Scarlet", "H", "X"],
    6 : ["(6)", "Mrs. White", "H", "X"],
    7 : ["(7)", "Candlestick", "???", "X"],
    8 : ["(8)", "Knife", "???", "X"],
    9 : ["(9)", "Lead Pipe", "???", "X"],
    10 : ["(10)", "Revolver", "H", "X"],
    11 : ["(11)", "Rope", "H", "X"],
    12 : ["(12)", "Wrench", "H", "X"],
    13 : ["(13)", "Hall", "???", "X"],
    14 : ["(14)", "Lounge", "???", "X"],
    15 : ["(15)", "Dining Room", "???", "X"],
    16 : ["(16)", "Kitchen", "???", "X"],
    17 : ["(17)", "Ball Room", "???", "X"],
    18 : ["(18)", "Conservatory", "???", "X"],
    19 : ["(19)", "Billiard Room", "H", "X"],
    20 : ["(20)", "Library", "H", "X"],
    21 : ["(21)", "Study", "H", "X"]}
	return cDeck

### DEBUG HAND FOR PLAYER
def deal_player_debug_hand():
	global playerDeck
	playerDeck = {
	1 : ["(1)", "Mr. Green", "???", "X"],
    2 : ["(2)", "Col. Mustard", "In hand", "X"],
    3 : ["(3)", "Mrs. Peacock", "In hand", "X"],
    4 : ["(4)", "Prof. Plum", "???", "X"],
    5 : ["(5)", "Miss Scarlet", "???", "X"],
    6 : ["(6)", "Mrs. White", "???", "X"],
    7 : ["(7)", "Candlestick", "???", "X"],
    8 : ["(8)", "Knife", "In hand", "X"],
    9 : ["(9)", "Lead Pipe", "In hand", "X"],
    10 : ["(10)", "Revolver", "???", "X"],
    11 : ["(11)", "Rope", "???", "X"],
    12 : ["(12)", "Wrench", "???", "X"],
    13 : ["(13)", "Hall", "???", "X"],
    14 : ["(14)", "Lounge", "In hand", "X"],
    15 : ["(15)", "Dining Room", "In hand", "X"],
    16 : ["(16)", "Kitchen", "In hand", "X"],
    17 : ["(17)", "Ball Room", "In hand", "X"],
    18 : ["(18)", "Conservatory", "In hand", "X"],
    19 : ["(19)", "Billiard Room", "???", "X"],
    20 : ["(20)", "Library", "???", "X"],
    21 : ["(21)", "Study", "???", "X"]}
	return cDeck
'''

#determine movable locations - for player or comp
def determine_movable_locations(user):
	global strLocationsPossible
	global cLoc
	global playerLocation
	global r
	global validOptions
	if user == 'player':
		loc = playerLocation
	elif user == 'comp':
		loc = cLoc
	if loc == 13:
		strLocationsPossible = "Study (21) or the Lounge (14)"
		validOptions = [13, 14, 21]
	elif loc == 21:
		strLocationsPossible = "Library (20) or the Hall (13)"
		validOptions = [13, 20, 21]
	else:
		strLocationsPossible = playerDeck[loc - 1][1] + " " + playerDeck[loc - 1][0] + " or " + playerDeck[loc + 1][1] + " " + playerDeck[loc + 1][0]
		validOptions = [loc - 1, loc, loc + 1]
	r = [strLocationsPossible, validOptions]
	return r

# make the player choose a room to guess from - house rules! player can only move to a room next to the one they're in. ***need to add secret passages***
def make_player_move():
	global playerLocation
	global r
	determine_movable_locations('player')
	strLocationsPossible = r[0]
	validOptions = r[1]
	print "Time to make a move."
	print "You are currently in the " + playerDeck[playerLocation][1] + " " + playerDeck[playerLocation][0] + ". You may go to the " + strLocationsPossible + ", or you may stay where you are. You may also enter \"C\" to show your clue card.",
	playerWantedLocation = raw_input("Please enter a choice:")
	if playerWantedLocation.isalpha() == True:
		playerWantedLocation = playerWantedLocation.upper()
		if playerWantedLocation == "C":
			print_card(playerDeck)
			make_player_move()
		else:
			print "Sorry, you must enter a valid room number between 13 and 21, or the letter \"C\" to show your clue card."
			make_player_move()
	elif int(playerWantedLocation) < 13 or int(playerWantedLocation) > 21:
		print "Sorry, you must enter a valid room number between 13 and 21, or the letter \"C\" to show your clue card."
		make_player_move()
	else:
		if int(playerWantedLocation) in validOptions:
			playerLocation = int(playerWantedLocation)
			print "You are now in the " + playerDeck[playerLocation][1] + "."
			# after a valid move, show the main options
			show_options()
		else:
			print "Sorry, you can't move that far!"

def show_options():
    print "Enter \"G\" to make a guess, \"A\" to make an accusation, or \"C\" to show your clue card."
    command = raw_input("Enter a command:")
    command = command.upper()
    if command != "C" and command != "A" and command != "G":
        print "Sorry! Please enter the letter/number as shown (without quotes)."
        show_options()
    elif command == "C":
        print_card(playerDeck)
        show_options()
    elif command == "A":
        verifyAccuse = raw_input("Warning: this will end the game! Are you sure you're ready to J'ACCUZE?!?! Enter Y/N:")
        verifyAccuse = verifyAccuse.upper()
        if verifyAccuse == "Y":
            jaccuse_intro()
        else:
        	print "Sorry, that was not a Y or an N."
        	show_options()
    elif command == "G":
        make_player_guess()

# the player has indicated they want to guess and so we prompt them for their input
def make_player_guess():
	global playerLocation
	guessRoom = playerLocation
	print "Time to guess!"
	time.sleep(1)
	print_card(playerDeck)
	print "You are currently in the " + playerDeck[playerLocation][1] + " " + playerDeck[playerLocation][0] + ". Choose a character (1-6) and a weapon (7-13) to ask the computer. ",
	guessChar = raw_input("Guess a character (1-6):")
	if int(guessChar) not in range(1,7) or guessChar.isalpha() == True:
		print "Not a valid character number (1-6)!"
		time.sleep(1)
		make_player_guess()
	else:
		guessChar = int(guessChar)
		guessWeap = raw_input("Guess a weapon (7-12):")
		if int(guessWeap) not in range(7,13) or guessWeap.isalpha() == True:
			print "Not a valid weapon number (7-12)!"
			time.sleep(1)
			make_player_guess()
		else:
			guessWeap = int(guessWeap)
			check_player_guess(guessChar, guessWeap, guessRoom)

#right now, this function and the few others it calls are the entirety of the AI behavior
def check_player_guess(guessChar, guessWeap, guessRoom):
	global turns
	turns += 1
	compHasTypes = comp_has_types()
	guesses = [guessChar, guessWeap, guessRoom]
	print "The computer is looking through its cards..."
	#we want to check if the player is an idiot and has already asked about any of the comp's cards
	for c in cDeck:
		if c in guesses:
			if cDeck[c][3] == 'STP':
				comp_pick_card_to_show(c)
				break
	showCategory = comp_determine_show_category()
	print showCategory
	finalChoice = comp_pick_card(showCategory, guesses)
	comp_pick_card_to_show(finalChoice)

def comp_pick_card_to_show(finalChoice):
	if finalChoice == "null":
		print "Computer: Sorry, I haven't got any of those!"
		comp_take_turn()
	else:
		print "The Computer shows you " + playerDeck[finalChoice][1] + " " + playerDeck[finalChoice][0]
		playerDeck[finalChoice][2] = "Shown by Computer"
		cDeck[finalChoice][3] = 'STP'
		#switch to computer's turn
		comp_take_turn()

# AI prioritizes the category determined with comp_determine_show_category() below, runs through its card types by priority (e.g., show room-type cards first) and selects the first one that matches a player guess
def comp_pick_card(showCategory, guesses):
	finalChoice = 0
	turn = -1
	# it will make up to 3 passes trying to find a card that matches one of the player's guesses
	for cat in showCategory:
		# as we cycle, turn increases meaning we're flipping through less-preferred card-type categories
		turn += 1
		if showCategory[turn] == "C":
			for c in range(1,7):
				if cDeck[c][2] == "H":
					if c in guesses:
						finalChoice = c
						#debug print
						print "picked turn " + str(turn) + " and category " + showCategory[turn]
						break
		if showCategory[turn] == "W":
			for c in range(7,13):
				if cDeck[c][2] == "H":
					if c in guesses:
						finalChoice = c
						print "picked turn " + str(turn) + " and category " + showCategory[turn]
						break
		if showCategory[turn] == "R":
			for c in range(13,22):
				if cDeck[c][2] == "H":
					if c in guesses:
						finalChoice = c
						print "picked turn " + str(turn) + " and category " + showCategory[turn]
						break
		if finalChoice != 0:
			break
	if finalChoice == 0:
		finalChoice = "null"
	return finalChoice

# builds a list so we can check that the computer has all types of cards (C, W, R), so that if it doesn't we can skip some. i dont remember if i call this ever	
def comp_has_types():
	compHasTypes = []
	for c in cDeck:
		if c in range(1,7) and cDeck[c][2] == "H":
			compHasTypes.append("C")
		if c in range(7,13) and cDeck[c][2] == "H":
			compHasTypes.append("W")
		if c in range(13,22) and cDeck[c][2] == "H":
			compHasTypes.append("R")
	return compHasTypes

# determine the best type of card for the computer to show, returns list of preferences 1-3
def comp_determine_show_category():
	catOptions = []
	# these vars are more like ...PlayerProbablyHas
	charPlayerHas = 0
	weapPlayerHas = 0
	roomPlayerHas = 0
	for c in cDeck:
		if c in range(1,7) and (cDeck[c][2] == "???" or cDeck[c][2] == 'IPH' or cDeck[c][3] == 'STP'):
			charPlayerHas += 1
		if c in range(7,13) and (cDeck[c][2] == "???" or cDeck[c][2] == 'IPH' or cDeck[c][3] == 'STP'):
			weapPlayerHas += 1
		if c in range (13,22) and (cDeck[c][2] == "???" or cDeck[c][2] == 'IPH' or cDeck[c][3] == 'STP'):
			roomPlayerHas += 1
	charWeight = float(charPlayerHas) / 6.0
	weapWeight = float(weapPlayerHas) / 6.0
	roomWeight = float(roomPlayerHas) / 9.0
	charWeight = str(charWeight)
	weapWeight = str(weapWeight)
	roomWeight = str(roomWeight)
	catOptions.append(charWeight)
	catOptions.append(weapWeight)
	catOptions.append(roomWeight)
	# chooses the lowest weight. the best weight is the lowest, meaning that the AI thinks the player has the fewest of this type of card, so it's better to reveal one of that type
	bestWeight = str(float(min(catOptions)))
	#debug print
	print catOptions
	for o in catOptions:
		if o == bestWeight:
			if o == charWeight and o == weapWeight and o == roomWeight:
				tieBreaker = randint(0,2)
				if tieBreaker == 0:
					showCategory1 = "C"
					showCategory2 = "R"
					showCategory3 = "W"
				elif tieBreaker == 1:
					showCategory1 = "W"
					showCategory2 = "R"
					showCategory3 = "C"
				elif tieBreaker == 2:
					showCategory1 = "R"
					showCategory2 = "C"
					showCategory3 = "W"
				break
			elif o == charWeight and o == weapWeight:
				showCategory3 = "R"
				if randint(0,1) == 0:
					showCategory1 = "W"
					showCategory2 = "C"
				else:
					showCategory1 = "C"
					showCategory2 = "W"
				break
			elif o == charWeight and o == roomWeight:
				showCategory3 = "W"
				if randint(0,1) == 0:
					showCategory1 = "C"
					showCategory2 = "R"
				else:
					showCategory1 = "R"
					showCategory2 = "C"
				break
			elif o == weapWeight and o == roomWeight:
				showCategory3 = "C"
				if randint(0,1) == 0:
					showCategory1 = "W"
					showCategory2 = "R"
				else:
					showCategory1 = "R"
					showCategory2 = "W"
				break
			elif o == charWeight:
				showCategory1 = "C"
				catOptions.remove(bestWeight)
				newBestWeight = str(float(min(catOptions)))
				if weapWeight == newBestWeight and roomWeight == newBestWeight:
					if randint(0,1) == 0:
						showCategory2 = "R"
						showCategory3 = "W"
					else:
						showCategory2 = "W"
						showCategory3 = "R"
					break
				elif weapWeight == newBestWeight:
					showCategory2 = "W"
					showCategory3 = "R"
				elif roomWeight == newBestWeight:
					showCategory2 = "R"
					showCategory3 = "W"
				break
			elif o == weapWeight:
				showCategory1 = "W"
				catOptions.remove(bestWeight)
				newBestWeight = str(float(min(catOptions)))
				if charWeight == newBestWeight and roomWeight == newBestWeight:
					if randint(0,1) == 0:
						showCategory2 = "C"
						showCategory3 = "R"
					else:
						showCategory2 = "R"
						showCategory3 = "C"
					break
				elif charWeight == newBestWeight:
					showCategory2 = "C"
					showCategory3 = "R"
				elif roomWeight == newBestWeight:
					showCategory2 = "R"
					showCategory3 = "C"
				break
			elif o == roomWeight:
				showCategory1 = "R"
				catOptions.remove(bestWeight)
				newBestWeight = str(float(min(catOptions)))
				if charWeight == newBestWeight and weapWeight == newBestWeight:
					if randint(0,1) == 0:
						showCategory2 = "C"
						showCategory3 = "W"
					else:
						showCategory2 = "W"
						showCategory3 = "C"
					break
				elif charWeight == newBestWeight:
					showCategory2 = "C"
					showCategory3 = "W"
				elif weapWeight == newBestWeight:
					showCategory2 = "W"
					showCategory3 = "C"
				break
	return [showCategory1, showCategory2, showCategory3]

'''
turn priorities:
1) accuse if certain
2) move to a room for guessing
	a) if room is known, use that 'killer' room or room card in hand not shown to player
			- this decision is part of the computer's move function
	b) if current room is in-hand, try to move to a room that is not known.
	c) if current room is in-hand and adjacent rooms are in-hand, try to move towards the nearest unknown room
2) pick cards to guess
	a) if 'killer' cards known from category (char or weap), use 'killer' cards or random cards in hand not shown to player
	b) otherwise, pick random unknown cards
4) make guess
'''

def comp_knows_char():
	global cDeck
	lst = []
	for c in range(1,7):
		if cDeck[c][2] == "KLR":
			return 1
		if cDeck[c][2] == "???":
			lst.append(c)
	if len(lst) == 1:
		killerCard = lst[0]
		cDeck[killerCard][2] = 'KLR'
		return 1
	else:
		return 0
		
def comp_knows_weap():
	global cDeck
	lst = []
	for c in range(7,13):
		if cDeck[c][2] == "KLR":
			return 1
		if cDeck[c][2] == "???":
			lst.append(c)
	if len(lst) == 1:
		killerCard = lst[0]
		cDeck[killerCard][2] = 'KLR'
		return 1
	else:
		return 0
		
def comp_knows_room():
	global cDeck
	lst = []
	for c in range(13,22):
		if cDeck[c][2] == "KLR":
			return 1
		if cDeck[c][2] == "???":
			lst.append(c)
	if len(lst) == 1:
		killerCard = lst[0]
		cDeck[killerCard][2] = 'KLR'
		return 1
	else:
		return 0

def comp_check_accuse_ready():
	if comp_knows_char() == 1 and comp_knows_room() == 1 and comp_knows_weap() == 1:
		print "Computer: I am ready to accuse"
		return 1
	else:
		print "Computer: I am not ready to accuse."
		return 0

#returns a list of guess cards
def comp_pick_guess_cards():
	global bCompTrickingForWeap
	global bCompTrickingForChar
	global bCompTrickingForRoom
	global cLoc
	if bCompTrickingForRoom == 1:
		print "COMPUTER TRICKING FOR ROOM"
	print "Computer's deck:"
	print_card(cDeck)
	bCompTrickingForWeap = 0
	bCompTrickingForChar = 0
	guessCards = []
	lstGuessCards = []
	lstGuessesChar = []
	lstGuessesWeap = []
	guessChar = 0
	guessWeap = 0
	# create lists of ??? cards
	for c in range(1,7):
		if cDeck[c][2] == "???":
			lstGuessesChar.append(c)
	for c in range(7,13):
		if cDeck[c][2] == "???":
			lstGuessesWeap.append(c)
	print "comp choices for chars: " + str(lstGuessesChar) + " comp choices for weap: " + str(lstGuessesWeap)
	# does comp know any killer cards?
	if comp_knows_char() == 1 and comp_knows_weap() == 1:
		print "I know char and weap -- I hope I picked the right spot."
		guessChar = random.choice(range(1,7))
		# don't pick cards shown by player already, or cards shown to player already as this would tip player off that comp knows killer card
		while cDeck[guessChar][2] == 'IPH' or cDeck[guessChar][3] == 'STP':
			guessChar = random.choice(range(1,7))
		guessWeap = random.choice(range(7,13))
		while cDeck[guessWeap][2] == 'IPH' or cDeck[guessWeap][3] == 'STP':
			guessWeap = random.choice(range(7,13))
		guessCards = [guessChar, guessWeap, cLoc]
		comp_make_guess(guessCards)
	if comp_knows_char() == 1:
		print "I know char (but not weap)"
		guessChar = random.choice(range(1,7))
		while cDeck[guessChar][2] == 'IPH' or cDeck[guessChar][3] == 'STP':
			guessChar = random.choice(range(1,7))
		# if it knows the character, pick a random unknown weapon
		guessWeap = random.choice(range(7,13))
		while cDeck[guessWeap][2] != '???':
			guessWeap = random.choice(range(7,13))
		guessCards = [guessChar, guessWeap, cLoc]
		comp_make_guess(guessCards)
	if comp_knows_weap() == 1:
		print "I know weap (but not char)"
		guessWeap = random.choice(range(7,13))
		while cDeck[guessWeap][2] == 'IPH' or cDeck[guessWeap][3] == 'STP':
			guessWeap = random.choice(range(7,13))
		guessChar = random.choice(range(1,7))
		# pick a random unknown character
		while cDeck[guessChar][2] != '???':
			guessChar = random.choice(range(1,7))
		guessCards = [guessChar, guessWeap, cLoc]
		comp_make_guess(guessCards)
	else:
		print "I dont know shit"
		#only pull the 'trick' if the room guess (aka comp location) is in hand and you only have 2 unknowns for the category
		# is the room comp is in in its own hand?
		if cDeck[cLoc][2] == 'H':
			if len(lstGuessesChar) == 2 and not len(lstGuessesWeap) <= 2:
				time.sleep(1)
				print "The computer scratches its ear."
				bCompTrickingForChar = 1
				guessWeap = random.choice(range(7,13))
				while cDeck[guessWeap][2] != 'H':
					guessWeap = random.choice(range(7,13))
				guessChar = random.choice(range(1,7))
				while cDeck[guessChar][2] == 'IPH' or cDeck[guessChar][3] == 'STP' or cDeck[guessChar][2] == 'H':
					guessChar = random.choice(range(1,7))
			elif len(lstGuessesWeap) == 2 and not len(lstGuessesChar) <= 2:
				time.sleep(1)
				print "The computer's eyebrow twitches."
				bCompTrickingForWeap = 1
				guessChar = random.choice(range(1,7))
				while cDeck[guessChar][2] != 'H':
					guessChar = random.choice(range(1,7))
				guessWeap = random.choice(range(7,13))
				while cDeck[guessWeap][2] == 'IPH' or cDeck[guessWeap][3] == 'STP' or cDeck[guessWeap][2] == 'H':
					guessWeap = random.choice(range(7,13))
			elif len(lstGuessesWeap) == 2 and len(lstGuessesChar) == 2:
				time.sleep(1)
				print "Computer: \"Sometimes, you gotta roll the tricky six.\""
				if randint(0,1) == 0:
					time.sleep(1)
					print "The computer scratches its ear."			
					bCompTrickingForChar = 1
					guessWeap = random.choice(range(7,13))
					while cDeck[guessWeap][2] != 'H':
						guessWeap = random.choice(range(7,13))
					guessChar = random.choice(range(1,7))
					while cDeck[guessChar][2] == 'IPH' or cDeck[guessChar][3] == 'STP' or cDeck[guessChar][2] == 'H':
						guessChar = random.choice(range(1,7))
				else:
					time.sleep(1)
					print "The computer's eyebrow twitches."
					bCompTrickingForWeap = 1
					guessChar = random.choice(range(1,7))
					while cDeck[guessChar][2] != 'H':
						guessChar = random.choice(range(1,7))
					guessWeap = random.choice(range(7,13))
					while cDeck[guessWeap][2] == 'IPH' or cDeck[guessWeap][3] == 'STP' or cDeck[guessWeap][2] == 'H':
						guessWeap = random.choice(range(7,13))
			#this is if the room is in-hand but it's not sure enough to try and trick for char or weap
			else:
				if guessChar == 0:
					guessChar = random.choice(lstGuessesChar)
				if guessWeap == 0:
					guessWeap = random.choice(lstGuessesWeap)
		#this is if the room is not in-hand; this is where most turns will make their guesses
		else:
			if guessChar == 0:
				guessChar = random.choice(lstGuessesChar)
			if guessWeap == 0:
				guessWeap = random.choice(lstGuessesWeap)
		print guessCards
		guessCards = [guessChar, guessWeap, cLoc]
		comp_make_guess(guessCards)

def comp_take_turn():
	#run elimination checks to replace ???s with IPHs if KLR card known for cat - this could prob be its own function
	for c in range(1,7):
		if cDeck[c][2] == "KLR":
			for i in range(1,7):
				if cDeck[c][2] == "???":
					cDeck[c][2] = "KLR"
	for c in range(7,13):
		if cDeck[c][2] == "KLR":
			for i in range(7,13):
				if cDeck[c][2] == "???":
					cDeck[c][2] = "KLR"
	for c in range(13,22):
		if cDeck[c][2] == "KLR":
			for i in range(13,22):
				if cDeck[c][2] == "???":
					cDeck[c][2] = "KLR"					
	global bCompTrickingForRoom
	time.sleep(1)
	print "It's the computer's turn!"
	print "The computer is in the " + cDeck[cLoc][0] + " " + cDeck[cLoc][1] + "."
	if comp_check_accuse_ready() == 1:
		comp_make_accusation()
	else:
		comp_choose_move()

def comp_choose_move():
	print "~~~ COMP_CHOOSE_MOVE ~~~"
	global cLoc
	global r
	determine_movable_locations('comp')
	validOptions = r[1]
	print "the computer is moving... its options are: " + str(validOptions)
	#first we check if it's worth tricking
	charsUnknown = comp_list_unknowns("char")
	weapsUnknown = comp_list_unknowns("weap")
	roomsUnknown = comp_list_unknowns("room")
	locBreakdown = comp_analyze_location(cLoc)
	''' FIX THIS SHIT
	#if we somehow ended up in a room already shown to us, let's get the hell out of there
	if cDeck[cLoc][2] == 'IPH':
		print
		moveMod = random_direction()
		if cDeck[cLoc + moveMod][2] == 'H'
		
		finalRoomChoice = cLoc + moveMod
		comp_make_move(finalRoomChoice)
	'''
	#should we stay in place and trick for something else? only if we have few of another cat and current room is in-hand
	#remember [list].count(item), [list].index(item)
	# we need to only move to an IPH if we're surrounded by them and know weap and char, to escape our current trap
	testWaters = []
	#if all choices are IPH
	if locBreakdown[1] == 'KLR':
		comp_make_move('stay')
	if locBreakdown[1] == 'IPH':
		if locBreakdown[0] == 'IPH' and locBreakdown[2] == 'IPH':
			print "I FUCKING HATE THIS ROOM."
			if comp_test_waters('back', 'IPH', 0) == comp_test_waters('fwd', 'IPH', 0):
				print "I am royally fucked here."
				#random move
				if randint(0,1) == 0:
					comp_make_move('back')
				else:
					comp_make_move('fwd')			
			if comp_test_waters('back', 'IPH', 0) < comp_test_waters('fwd', 'IPH', 0):
				comp_make_move('back')
			else:
				comp_make_move('fwd')
	elif locBreakdown[0] == 'IPH' and locBreakdown[2] == 'IPH':
		if comp_knows_char() == 1 and comp_knows_room == 1:
			#we gotta waste a turn unfortunately or we'll be stuck here forever
			if comp_test_waters('back', 'IPH', 0) == comp_test_waters('fwd', 'IPH', 0):
				print "I am royally fucked here."
				#random move
				if randint(0,1) == 0:
					comp_make_move('back')
				else:
					comp_make_move('fwd')	
			if comp_test_waters('back', 'IPH', 0) < comp_test_waters('fwd', 'IPH', 0):
				comp_make_move('back')
			else:
				comp_make_move('fwd')	
		else:
			comp_make_move('stay')
	elif locBreakdown[0] == 'IPH':
		comp_make_move('fwd')
	elif locBreakdown[2] == 'IPH':
		comp_make_move('back')
	#if there's no IPHs next to cLoc
	else:
		if locBreakdown[1] == 'H' and (len(charsUnknown) == 2 or len(weapsUnknown) == 2):
			print "Hopefully, I will be pulling a trick."
			comp_make_move('stay')
		#is there an IPH after an adjacent room? if so, move to it
		locBackBreakdown = comp_analyze_location(cLoc - 1)
		if locBackBreakdown[0] == 'IPH' and locBreakdown[0] == '???':
			print "closing gap backwards"
			comp_make_move('back')
		locFwdBreakdown = comp_analyze_location(cLoc + 1)
		if locFwdBreakdown[2] == 'IPH' and locBreakdown[2] == '???':
			print "closing gap forwards"
			comp_make_move('fwd')
		# this is where most turns will make their move
		else:
			print "regular movement choice"
			if comp_test_waters('back', '???', 0) > comp_test_waters('fwd', '???', 0):
				comp_make_move('back')
			elif comp_test_waters('back', '???', 0) < comp_test_waters('fwd', '???', 0):
				comp_make_move('fwd')
			else:
				if randint(0,1) == 0:
					comp_make_move('back')
				else:
					comp_make_move('fwd')
	'''
	if cDeck[cLoc][2] == 'H':
		# are we surrounded by IPHs?
		if locBreakdown[0] == 'IPH' and locBreakdown[2] == 'IPH':
			comp_make_move
		#maybe here we make the trick choice
		#insert trickery
		#if we're in an H and surrounded by Hs
		if locBreakdown.count('H') == 3:
			backwards1 = comp_analyze_location(cLoc - 1)
			forwards1 = comp_analyze_location(cLoc + 1)
			if backwards1.count('???') > forwards1.count('???'):
	'''
				
def comp_test_waters(dir, item, wantsList):
	if dir == 'back':
		# this list is [farthest -> nearest]
		testWatersBack = comp_analyze_location(cLoc - 3)
		print testWatersBack
		del testWatersBack[1]
		del testWatersBack[1]
		for i in comp_analyze_location(cLoc - 2):
			testWatersBack.append(i)
		del testWatersBack[2]
		del testWatersBack[2]
		for i in comp_analyze_location(cLoc - 1):
			testWatersBack.append(i)
		del testWatersBack[3]
		print "testwatersback: " + str(testWatersBack)
		if wantsList == 1:
			return testWatersBack
		else:
			return testWatersBack.count(item)
	if dir == 'fwd':
		# this list is [nearest -> farthest]
		testWatersFwd = comp_analyze_location(cLoc - 3)
		print testWatersFwd
		del testWatersFwd[0]
		del testWatersFwd[0]
		for i in comp_analyze_location(cLoc - 2):
			testWatersFwd.append(i)
		del testWatersFwd[1]
		del testWatersFwd[1]
		for i in comp_analyze_location(cLoc - 1):
			testWatersFwd.append(i)
		del testWatersFwd[2]
		print "testwatersfwd: " + str(testWatersFwd)
		if wantsList == 1:
			return testWatersBack
		else:
			return testWatersFwd.count(item)
	
def random_direction():
	dir = randint(-1,1)
	while dir == 0:
		dir = randint(-1,1)
	return dir

def comp_analyze_location(loc):
	lst = []
	if loc < 12 or loc > 23:
		print "Tried to analyze location too far away."
	if loc == 12:
		loc = 21
	if loc == 11:
		loc = 20
	if loc == 22:
		loc = 13
	if loc == 23:
		loc = 14
	if loc == 13:
		return [cDeck[21][2], cDeck[13][2], cDeck[14][2]]
	if loc == 21:
		return [cDeck[20][2], cDeck[21][2], cDeck[13][2]]
	return [cDeck[loc - 1][2], cDeck[loc][2], cDeck[loc + 1][2]]
	
def random_move_stay():
	moveMod = randint(-1,1)
	return moveMod
	
def comp_make_move(dir):
	print "~~~ COMP_MAKE_MOVE ~~~"
	global cLoc
	global r
	determine_movable_locations('comp')
	validOptions = r[1]
	if dir == 'back':
		cLoc = validOptions[0]
	elif dir == 'fwd':
		cLoc = validOptions[2]
	comp_pick_guess_cards()

def comp_list_unknowns(cat):
	lst = []
	if cat == "char":
		for i in range(1,7):
			if cDeck[i][2] == "???":
				lst.append(i)
	elif cat == "weap":
		for i in range(7,13):
			if cDeck[i][2] == "???":
				lst.append(i)
	elif cat == "room":
		for i in range(13,22):
			if cDeck[i][2] == "???":
				lst.append(i)
	return lst	
	
def comp_make_guess(guessCards):
	print "~~~ COMP_MAKE_GUESS ~~~"
	print guessCards
	print "Computer guesses: Character: " + cDeck[guessCards[0]][1] + ", Weapon: " + cDeck[guessCards[1]][1] + ", Room: " + cDeck[guessCards[2]][1]
	make_player_show(guessCards)

def make_player_show(guessCards):
	print "~~~ MAKE PLAYER SHOW ~~~"
	global bPlayerHasNone
	print_card(playerDeck)
	print "The computer guessed " + str(guessCards)
	haveChecker = 0
	for i in guessCards:
		if playerDeck[i][2] == "In hand":
			haveChecker += 1
	###DEBUG
	print "haveChecker: " + str(haveChecker)
	if haveChecker == 0:
		print "Uh-oh! You don't have any of those!"
		comp_update_deck(guessCards, 0)
	else:
		print "What card would you like to show the computer?",
		cardToShow = int(raw_input('Choose a card:'))
		print "You showed the computer " + playerDeck[cardToShow][1] + "."
		comp_update_deck(guessCards, cardToShow)
		
def comp_update_deck(guessCards, cardToShow):
	global bCompTrickingForChar
	global bCompTrickingForWeap
	global bCompTrickingForRoom
	guessedChar = guessCards[0]
	guessedWeap = guessCards[1]
	guessedRoom = guessCards[2]
	print "The computer scratches on its clue card..."
	#debug
	print "tricks: char/weap/room: " + str(bCompTrickingForChar) + str(bCompTrickingForWeap) + str(bCompTrickingForRoom)
	print "guesscards: " + str(guessCards)
	time.sleep(1)
	#was the computer pulling a trick?
	if bCompTrickingForChar == 1 or bCompTrickingForWeap == 1 or bCompTrickingForRoom == 1:
		print "computer pulled a trick!"
		#did the player have none of the guessed cards?
		if cardToShow == 0:
			if bCompTrickingForChar == 1:
				print "tricked for char, guessed:" + str(guessCards[0])
				for i in range(1,7):
					if cDeck[i][2] == "???":
						if i not in guessCards:
							cDeck[i][2] = "IPH"
							cDeck[i][3] = "DBT"
						if i in guessCards:
							cDeck[i][2] = "KLR"
				print "trick update complete."
			elif bCompTrickingForWeap == 1:
				print "tricked for weap, guessed:" + str(guessCards[1])
				for i in range(7,13):
					if cDeck[i][2] == "???":
						if i not in guessCards:
							cDeck[i][2] = "IPH"
							cDeck[i][3] = "DBT"
						if i in guessCards:
							cDeck[i][2] = "KLR"
				print "trick update complete."
			elif bCompTrickingForRoom == 1:
				print "tricked for room, guessed:" + str(guessCards[2])
				for i in range(13,22):
					if cDeck[i][2] == "???":
						if i not in guessCards:
							cDeck[i][2] = "IPH"
							cDeck[i][3] = "DBT"
						if i in guessCards:
							cDeck[i][2] = "KLR"
				print "trick update complete."
			make_player_move()
		# if player had a guessed card
		else:
			print "I tricked but nothing special happened"
			for i in range(1,22):
				if i in guessCards:
					if cDeck[i][2] == '???':
						cDeck[i][2] = 'SBP'
						cDeck[i][3] = 'DBT'
			make_player_move()
	#computer wasn't tricking
	else:
		if cardToShow == 0:
			print "jackpot"
			for i in cDeck:
				if cDeck[guessedChar][2] == '???':
					cDeck[guessedChar][2] = "KLR"
					for i in range(1,7):
						if cDeck[i][2] == '???':
							print "I scratched off " + cDeck[i][0]
							cDeck[i][2] = 'IPH'
							cDeck[i][3] = 'LCK'
				if cDeck[guessedWeap][2] == '???':
					cDeck[guessedWeap][2] = "KLR"
					for i in range(7,13):
						if cDeck[i][2] == '???':
							print "I scratched off " + cDeck[i][0]
							cDeck[i][2] = 'IPH'
							cDeck[i][3] = 'LCK'
				if cDeck[guessedRoom][2] == '???':
					cDeck[guessedRoom][2] = "KLR"
					for i in range(13,22):
						if cDeck[i][2] == '???':
							print "I scratched off " + cDeck[i][0]
							cDeck[i][2] = 'IPH'
							cDeck[i][3] = 'LCK'		
			make_player_move()
		else:
			print "regular update"
			cDeck[cardToShow][2] = 'IPH'
			make_player_move()

def comp_make_accusation():
	print "Placeholder - computer accuses"

# calls jaccuse() after some text effects
def jaccuse_intro():
	print "J'Accuse!",
	time.sleep(0.3)
	print ".",
	time.sleep(0.3)
	print ".",
	time.sleep(0.3)
	print ".",
	time.sleep(1)
	print "!!!"
	time.sleep(0.5)
	jaccuse()

# function called when players decide to make an accusation
def	jaccuse():
	global kChar
	global kWeap
	global kRoom
	print_card(playerDeck)
	print "Whom do you j'accuse?!",
	accuseChar = raw_input("Enter a character (1-6):")
	if int(accuseChar) not in range(1,7) or accuseChar.isalpha() == True:
		print "Not a valid character number (1-6)!"
		time.sleep(1)
		jaccuse()
	else:
		print "With what do you j'accuse they did the deadly deed?!",
		accuseWeap = raw_input("Guess a weapon (7-12):")
		if int(accuseWeap) not in range(7,13) or accuseWeap.isalpha() == True:
			print "Not a valid weapon number (7-12)!"
			time.sleep(1)
			jaccuse()
		else:
			print "And where was this horrible crime committed?!",
			accuseRoom = raw_input("Guess a room (13-21):")
			if int(accuseRoom) not in range(13,22) or accuseRoom.isalpha() == True:
				print "Not a valid room number (13-21)!"
				time.sleep(1)
				jaccuse()
			else:
				print "Sacre bleu! You have accused " + playerDeck[int(accuseChar)][1] + " of killing Mr. Body in the " + playerDeck[int(accuseRoom)][1] + " with the " + playerDeck[int(accuseWeap)][1] + "!"
				time.sleep(2)
				if int(accuseChar) == kChar and int(accuseWeap) == kWeap and int(accuseRoom) == kRoom:
					print "You, monsieur, are a master detective. You win!"
					print "You took " + str(turns) + " turns."
					print "G A M E   O V E R"
				else:
					print "I am so sorry, monsieur, it seems your detective skills were not up to par. It was, in fact, the despicable " + playerDeck[kChar][1] + " who commited the murder in the " + playerDeck[kRoom][1] + " with the " + playerDeck[kWeap][1] + ". Better luck next time!"
					print "You took " + str(turns) + " turns."
					print "G A M E   O V E R"	

#deal_player_debug_hand()
deal_player_hand(handsize)
#deal_comp_debug_hand()
deal_comp_hand()
comp_choose_move()