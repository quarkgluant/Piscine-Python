from django.db import models
# • title : chaine de character, unique, d’une taille maximale de 64 octets, non nul.
# • episode_nb : entier, PRIMARY KEY.
# • opening_crawl : texte - peut etre nul.
# • director : chaîne de caractères d’une taille maximale de 32 octets, non nul.
# • producer : chaîne de caractères d’une taille maximale de 128 octets, non nul.
# • release_date : date (sans l’heure), non nul.
# Ce modèle doit également redéfinir la methode __str__ afin que celle-ci renvoie l’attribut
# title
# Create your models here.
class Movies(models.Model):
	title = models.CharField(max_length = 64, unique = True)
	episode_nb = models.AutoField(primary_key=True)
	opening_crawl = models.TextField(blank=True)
	director = models.CharField(max_length = 32)
	producer = models.CharField(max_length = 128)
	release_date = models.DateField()

	def __str__(self):
		return self.title
