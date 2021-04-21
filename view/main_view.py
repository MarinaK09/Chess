
from model.tournament import Tournament
from model.player import Player



class MainView :

	def __init__(self) :
		self.newtournament = Tournament()
		self.first_player = Player()
		self.second_player = Player()
		self.third_player = Player()
		self.fourth_player = Player()

	def main_menu(self) : 

		#Principal menu: User is asked to make a choice
		print ("---------------welcome---------------")
			
		print("""
		Please choose an option: 
		1 : Create a new tournament
		2 : Continue a tournament 
		3 : Create a new player 
		4 : Generate a report
		5 : Quit""")

		# " if isdigit() à chercher...else"
		action = input()
		return action

	def new_player(self) :
			#Player creation
		self.first_player.setfirstname(input("Firstname: "))
		self.first_player.setlastname(input("Lastname: "))
		self.first_player.setbirthdate(input("Birthdate: "))
		self.first_player.setsexe(input("Sexe: "))
		self.first_player.setranking(input("Ranking: "))

	def new_tournament(self) :
			#Tournament creation
		self.newtournament.setname(input("Tournament name: "))
		self.newtournament.setsite(input("Site: "))
		self.newtournament.setdate(input("Date: "))
		self.newtournament.setroundnumber(input("Round: "))
		self.newtournament.settimecontrol(input("Time control: "))
		self.newtournament.setdescription(input("Description: "))
		players = print("""
		Type 1 to: Add an existing player
		Type 2 to: Create a new player""")
		
		players = input()
		if players == "1" :
			print("No")
		elif players == "2" :
			# Adding the 1st player
			print("----Player 1----")
			self.first_player.setfirstname(input("Firstname: "))
			self.first_player.setlastname(input("Lastname: "))
			self.first_player.setbirthdate(input("Birthdate: "))
			self.first_player.setsexe(input("Sexe: "))
			self.first_player.setranking(input("Ranking: "))
			self.first_player.player_serialization(self.first_player)
			self.newtournament.setfirstplayer(self.first_player)
			
			# Adding the 2nd player
			print("----Player 2----")
			self.second_player.setfirstname(input("Firstname: "))
			self.second_player.setlastname(input("Lastname: "))
			self.second_player.setbirthdate(input("Birthdate: "))
			self.second_player.setsexe(input("Sexe: "))
			self.second_player.setranking(input("Ranking: "))
			self.second_player.player_serialization(self.second_player)
			self.newtournament.setsecondplayer(self.second_player)

			# Adding the 3rd player
			print("----Player 3----")
			self.third_player.setfirstname(input("Firstname: "))
			self.third_player.setlastname(input("Lastname: "))
			self.third_player.setbirthdate(input("Birthdate: "))
			self.third_player.setsexe(input("Sexe: "))
			self.third_player.setranking(input("Ranking: "))
			self.third_player.player_serialization(self.third_player)
			self.newtournament.setthirdplayer(self.third_player)

			# Adding the 4th player
			print("----Player 4----")
			self.fourth_player.setfirstname(input("Firstname: "))
			self.fourth_player.setlastname(input("Lastname: "))
			self.fourth_player.setbirthdate(input("Birthdate: "))
			self.fourth_player.setsexe(input("Sexe: "))
			self.fourth_player.setranking(input("Ranking: "))
			self.fourth_player.player_serialization(self.fourth_player)
			self.newtournament.setfourthplayer(self.fourth_player)
		else :
			print("Choose 1 or 2 please")




