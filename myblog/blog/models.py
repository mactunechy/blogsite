from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length= 120)
	content = models.TextField(max_length = 1500)
	pub_date = models.DateTimeField(auto_now=True)
	modified_date = models.DateTimeField(auto_now_add=True)
	image = models.FileField( )
	def __str__(self):
		return self.title
		
		
		
class ContactForm(models.Model):
	name = models.CharField(max_length=120)
	email=models.EmailField(max_length=100)
	message= models.TextField( max_length=2000)	
	def __str__(self):
		return self.name
			