from model.player import Player
from tinydb import TinyDB


class Tournament:

	name                    = ""
	__site                  = ""
	__date                  = ""
	__roundnumber           = ""
	__first_player          = Player()
	__second_player         = Player()
	__third_player          = Player()
	__fourth_player         = Player()
	__timecontrol           = ""
	__description           = ""

	def __init__(self) :
		pass

    # Setters
	def setname(self, name) :
		self.__name = name
	def setsite(self, site) :
		self.__site = site
	def setdate(self, date) :
 		self.__date = date
	def setroundnumber(self, roundnumber) :
 		self.__roundnumber = roundnumber
	def setfirstplayer(self, player) :
 		self.__first_player= player
	def setsecondplayer(self, player) :
 		self.__first_player= player
	def setthirdplayer(self, player) :
 		self.__first_player= player
	def setfourthplayer(self, player) :
 		self.__first_player= player
	def settimecontrol(self, timecontrol) :
 		self.__timecontrol= timecontrol
	def setdescription(self, description) :
 		self.__description= description

    # Getters

	def getname(self) :
		return self.__name
	def getsite(self) :
		return self.__site
	def getdate(self) :
 		return self.__date
	def getroundnumber(self) :
 		return self.__roundnumber
	def get_first_player(self, player) :
 		self.__first_player
	def get_second_player(self, player) :
 		return self.__first_player
	def get_third_player(self, player) :
 		return self.__first_player
	def get_fourth_player(self, player) :
 		return self.__first_player
	def getranking(self) :
 		return self.__timecontrol
	def getdescription(self) :
 		return self.__description

    # tournament serialization method
	def tournament_serialization(self, tournament):
		self.serializedtournament = {
							'firstname': tournament.setfirstname, 
							'lastname': tournament.setlastname,
							'birthdate': tournament.setbirthdate,
							'sexe': tournament.setsexe,
							'ranking': tournament.setranking  
									}
		db = TinyDB('db.json')
		tournaments_table = db.table('tournaments')
		tournaments_table.truncate()	# clear the table first
		tournaments_table.insert(self.serializedtournament)