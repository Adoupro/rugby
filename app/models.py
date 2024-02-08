from django.db import models

# Create your models here.
class Player(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.last_name} - {self.first_name}"