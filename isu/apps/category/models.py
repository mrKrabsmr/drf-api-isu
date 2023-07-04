from django.db import models


class Category(models.Model):
    """types = (
        (1, "service"),
        (2, "sales"),
        (3, "education"),
        (4, "trade"),
        (5, "logistics"),
        (6, "transport"),
        (7, "catering"),
        (8, "hotel business"),
        (9, "beauty and health"),
        (10, "marketing, advertising, PR"),
        (11, "finance, accounting, banks"),
        (12, "medicine"),
        (13, "manufacturing"),
        (14, "law"),
        (15, "cryptocurrencies"),
        (16, "tourism"),
        (17, "sport"),
        (18, "programming")
    )"""

    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to="media/category_logo", blank=True, null=True)
