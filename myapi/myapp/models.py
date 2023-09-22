from django.db import models

# 
class Music(models.Model):
    
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    rating = (
        ("10", "Perfect")
        ("9", "Almost Perfect")
        ("8", "Wonderful")
        ("7", "Great")
        ("6", "Cool")
        ("5", "Ok")
        ("4", "Bad")
        ("3", "Very Bad")
        ("2", "Trash")
        ("1", "The wost thing in the entire world")
        ("0", "Default")
        )
    
    music_rating = models.CharField(max_length=3, choices=rating, default='0')