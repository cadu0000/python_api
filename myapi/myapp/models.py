from django.db import models

class Music(models.Model):

    music_id = models.AutoField(primary_key=True, unique=True)
    music_name = models.CharField(max_length=120)
    seconds = models.IntegerField()
    singer = models.CharField(max_length=120)
    pub_date = models.DateField()
    url_picture = models.CharField(max_length=150, null=True)

    rating = (
        ("10", "Perfect"),
        ("9", "Almost Perfect"),
        ("8", "Wonderful"),
        ("7", "Great"),
        ("6", "Cool"),
        ("5", "Ok"),
        ("4", "Bad"),
        ("3", "Very Bad"),
        ("2", "Trash"),
        ("1", "The wost thing in the entire world"),
        ("0", "Default")
        )
    
    music_rating = models.CharField(max_length=3, choices=rating, default='0')

    def __str__(self):
        return Music(
            self.music_id,
            self.music_name,
            self.seconds,
            self.singer,
            self.pub_date,
            self.url_picture,
            self.music_rating
        )
    
    class Meta:
        db_table = 'musicdb'


class FindMusic(models.Model):

    name = models.ForeignKey(Music, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

