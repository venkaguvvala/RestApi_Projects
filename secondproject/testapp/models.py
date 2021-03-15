from django.db import models

# Create your models here.
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=60)
    DisplayFields=['title','author']
    SearchableFields=['author']
    FilterFields=['title']

    class Meta:
        db_table="Blog"
