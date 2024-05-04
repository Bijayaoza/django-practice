from django.db import models
from django.contrib.auth.models import User
# Create your models here.

### one to one relation
class Page(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    page_name=models.CharField(max_length=40)
    page_publish_date=models.DateField()

### many to  one relataion here User can do many post but post can be from only one user
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_title=models.CharField(max_length=90)

#### many to many relation here many user can write one song and one singer can song many songs
class Song(models.Model):
    user=models.ManyToManyField(User)
    song_name=models.CharField(max_length=90)
## this function helps to show the name of all user who wrote song  
    def song_written(self):
        return ', '.join([str(p) for p in self.user.all()] )

##here self will go to the root of class and .user.all() will give all the user who make song
### str(P) is an expression ie from python list comprehension concept it  will convert list into string and pass to the ','
#### this function is used in an list at admin t0 display user who make song