from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    RATING_SCORE = (
        ('5','5'),
        ('4','4'),
        ('3','3'),
        ('2','2'),
        ('1','1'),
    )

    watched = models.BooleanField(default=False)
    title = models.CharField(max_length = 50)
    rating = models.CharField(max_length = 10, choices=RATING_SCORE, blank=True, null=True)
    release_date = models.DateField()
    review = models.TextField(max_length=255)