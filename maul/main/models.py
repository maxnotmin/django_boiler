from django.db import models
from django.utils.timezone import now


# Create your models here.
class Services(models.Model):
    # Create a new model
    # Here we are description what we want our data to look like, what we may need
    # Each model will map to a database table
    # The default DB is Sqlite3
    # TO changes to the dir maul > settings.py > DATABASE

    # Primary key is set by default
    #CharField is a shorter field
    service_title = models.CharField(max_length=200)
    #TextField used for longer text items
    service_content = models.TextField()
    service_published = models.DateTimeField("date published")

