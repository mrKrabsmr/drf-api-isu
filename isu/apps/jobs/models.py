from django.db import models
from apps.category.models import Category

from apps.users.models import User


class Job(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="jobs")
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, related_name="jobs")
    body = models.TextField()
    post = models.CharField(max_length=250)
    salary_from = models.DecimalField()
    salary_up_to = models.DecimalField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "jobs"
        verbose_name = "job"
        verbose_name_plural = "jobs"

    def __str__(self) -> str:
        return f"{self.user} | job: {self.id}"



class JobImage(models.Model):
    job = models.ForeignKey(to=Job, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="media/job_images")

    