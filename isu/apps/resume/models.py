from django.db import models

from apps.users.models import User
from apps.category.models import Category


class Resume(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="resumes")
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, related_name="resumes")
    body = models.TextField()
    salary_expectations_from = models.DecimalField()
    salary_expectations_up_to = models.DecimalField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "resume"
        verbose_name = "resume"
        verbose_name_plural = "resume"
    

    def __str__(self) -> str:
        return f"{self.user} | resume: {self.id}"


class ResumeImage(models.Model):
    resume = models.ForeignKey(to=Resume, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="media/resume_images")

