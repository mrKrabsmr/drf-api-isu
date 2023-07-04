from django.db import models

from apps.users.models import User
from apps.category.models import Category


class Work(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="works")
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, related_name="works")
    body = models.TextField()
    term = models.DateTimeField()
    payment = models.DecimalField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "works"
        verbos_name = "work"
        verbos_name_plural = "works"

    
class WorkImage(models.Model):
    work = models.ForeignKey(to=Work, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="media/work_images")