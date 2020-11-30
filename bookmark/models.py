from django.db import models
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)  # 저장할 사이트 이름
    url = models.URLField('Site URL')  # 저장할 사이트 주소

    def __str__(self):
        #객체를 출력할 때 나타날 값
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    def get_absolute_url(self):
        return reverse('bookmark:detail', args=[str(self.id)])