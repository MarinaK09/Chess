from tinydb import TinyDB


class Player:

	firstname = ""
	lastname  = ""
	birthdate = ""
	sexe      = ""
	ranking   = ""

	def __init__(self) :
		pass

   # Setters
	def setfirstname(self, firstname) :
		self.firstname = firstname
	def setlastname(self, lastname) :                          
		self.lastname = lastname
	def setbirthdate(self, birthdate) :            
 		self.birthdate = birthdate                                    
	def setsexe(self, sexe) :          
 		self.sexe = sexe
	def setranking(self, ranking) :
 		self.ranking = ranking
		

   # Getters
	def getfirstname(self) :
		return self.firstname 
	def getlastname(self) :
		return self.lastname
	def getbirthdate(self) :
 		return self.birthdate
	def getsexe(self) :
 		return self.sexe
	def getranking(self) :
 		return self.ranking

     # Player serialization method
	def player_serialization(self, player):
		self.serializedplayer = {
							'firstname': player.firstname, 
							'lastname': player.lastname,
							'birthdate': player.birthdate,
							'sexe': player.sexe,
							'ranking': player.ranking  
									}
		db = TinyDB('db.json')
		players_table = db.table('players')
		players_table.truncate()	# clear the table first
		players_table.insert(self.serializedplayer)