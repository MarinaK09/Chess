class PlayerControler : #creer un fichier different

	def player_validation(self, player) :
		if self.__isValidPlayer(player) :
			pass

	def __isValidPlayer(self, player) :

		if player.getFirstname() != "" and player.getLastname() != "" and player.getBirthdate() != "" and player.getSexe() != "" :
			return True
		return False