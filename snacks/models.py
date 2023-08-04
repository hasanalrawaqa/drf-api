from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model


class Snack(models.Model):
    title = models.CharField(max_length=100)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating=models.IntegerField(default=3 , validators=[MinValueValidator(1), MaxValueValidator(10)])
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('snack_detail', args=[str(self.id)])