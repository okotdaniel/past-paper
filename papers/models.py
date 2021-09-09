from django.db import models


category = (
    ('biology','biology'),
    ('physics','physics'),
    ('chemistry','chemistry'),
)

# Create your models here.
class Papers(models.Model):
    name = models.CharField(
        max_length=100, 
        null=False,
        blank=False
    )

    file_path = models.FileField(
        upload_to='documents/papers'
        )

    date_created = models.DateField(
        auto_now=True
        )
    category = models.CharField(
        max_length=100,
        choices=category,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name