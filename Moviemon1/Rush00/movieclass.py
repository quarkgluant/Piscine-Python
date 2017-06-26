import sys, json, requests, pickle, random, os
from django.conf import settings


class Gestion(object):

	# mapx = 50
	# mapy = 50
	#
	# coord           = [48.8584, 2.2945]
	# movieballs      = 100
	# Moviemons       = {}
	# My_Moviemons    = []
	# MoviemonBattle  = ''
	# Strenght        = 0

	@classmethod
	def set_default(cls):

		cls.mapx = settings.POS_PLAYER[0]
		cls.mapy = settings.POS_PLAYER[1]
		cls.coord           = [0,0] #[48.8584, 2.2945]
		cls.movieballs      = 100
		cls.Moviemons       = {}
		cls.My_Moviemons    = []
		cls.MoviemonBattle  = ''
		cls.Strenght        = 0
		cls.index 			= 0

	@classmethod
	def set_value(cls,
					new_corrd,
					new_movieballs,
					new_Moviemons,
					new_My_Moviemons,
					new_MoviemonBattle = [],
					new_Strenght = 0,
					new_mapx = 0,
					new_mapy = 0,
					new_index = 0):

		cls.coord           = new_corrd
		cls.movieballs      = new_movieballs
		cls.Moviemons       = new_Moviemons
		cls.My_Moviemons    = new_My_Moviemons
		cls.MoviemonBattle  = new_MoviemonBattle
		cls.Strenght        = new_Strenght
		cls.mapx			= new_mapx
		cls.mapy            = new_mapy
		cls.index			= new_index

	@classmethod
	def move_coord(cls, x, y):
		coord[0] = x
		coord[1] = y

	@classmethod
	def modif_movieballs(cls, nb):
		cls.movieballs = nb

	@classmethod
	def add_moviemons(cls, name):
		cls.My_Moviemons.append(name)

	@classmethod
	def del_moviemons(cls, name):
		del cls.Moviemons[name]

	@classmethod
	def del_battlemovie(cls, moviemon_id):
		self.MoviemonBattle = ''

	def __init__(self):
		self.lst = settings.LIST_MOVIES

	def load(self, name):
		info = []
		print(name,os.path.isfile(name))
		if os.path.isfile(name):
			with (open(name, "rb")) as openfile:
				while True:
					try:
						print("Je recupere gentillement:", name);
						info.append(pickle.load(openfile))
					except EOFError:
						break
			self.set_value(info[0][0],
						   info[0][1],
						   info[0][3],
						   info[0][2],
						   info[0][4],
						   info[0][5],
						   info[0][6],
						   info[0][7],
						   info[0][8])
			self.save('info.pickle')
			openfile.close()
			return info[0]
		return ("Free")

	def dump(self):
		info = []
		with (open("info.pickle", "rb")) as openfile:
			while True:
				try:
					info.append(pickle.load(openfile))
				except EOFError:
					break
		openfile.close()
		return info[0]

	def get_random_movie(self):
		my_mon = self.My_Moviemons
		mon = list(self.Moviemons.keys())
		return [x for x in mon if x not in my_mon]

	def load_default_settings(self):
		self.set_default()
		F = open("info.pickle", "wb")
		for item in self.lst:
			r = requests.get("http://www.omdbapi.com/?t=" + item + "&apikey=3170a9e6")
			if r.status_code != 200:
				raise Exception ("Error: " + str(r.status_code))
			Moviemon = json.loads(r.text)
			self.Moviemons[Moviemon['Title'].replace(" ", "_").replace(":", "-")] = Moviemon
		info = [
				self.coord,
				self.movieballs,
				self.My_Moviemons,
				self.Moviemons,
				self.MoviemonBattle,
				self.Strenght,
				self.mapx,
				self.mapy,
				self.index
		]

		pickle.dump(info, F)
		F.close()
		return info

	@property
	def get_strength(self):
		return len(self.My_Moviemons)

	def get_movie(self, name):
		return self.Moviemons[name]

	def get_all_movies(self):
		info = self.dump()
		return list(info[3].keys())

	def save(self, name):
		F = open(name, "wb")
		info = [
				self.coord,
				self.movieballs,
				self.My_Moviemons,
				self.Moviemons,
				self.MoviemonBattle,
				self.Strenght,
				self.mapx,
				self.mapy,
				self.index
			]

		pickle.dump(info, F)
		F.close()
