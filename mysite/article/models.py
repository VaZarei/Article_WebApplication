from django.db import models
from django.urls import reverse

# Create your models here.

class ArticleDB(models.Model):
    Title = models.CharField(max_length=100)
    Body  = models.TextField()
    Auther= models.ForeignKey("auth.user", on_delete=models.CASCADE)


    def __str__(self):
        return self.Title
    
    def get_absolute_url(self):
        return reverse("article_DetailView_URL", kwargs={"pk": self.pk})
    
    