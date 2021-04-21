from view.main_view import MainView


class MainControler :

	def __init__(self) :
		self.choice_main_menu = ""
		self.main_view = MainView()

	def start(self) :	
		while self.choice_main_menu != "5" :
			self.choice_main_menu = self.main_view.main_menu()
			if self.choice_main_menu == "1" :
				self.main_view.new_tournament()