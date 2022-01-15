from django.db import models
from ckeditor.fields import RichTextField
from user.models import User
from urllib.parse import urlparse, parse_qs

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True,null=False)
    image = models.ImageField(upload_to='category/%Y/%m')

    def __str__(self) -> str:
        return self.name
class ModelBase(models.Model):
    class Meta:
        abstract = True
    subject = models.CharField(max_length=255, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    

    def __str__(self) -> str:
        return self.subject
    
class Course(ModelBase):
    class Meta:
        unique_together = ('subject', 'category')
    description = RichTextField(null=True)
    image = models.ImageField(upload_to='course/%Y/%m', default=None)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    user_register = models.ManyToManyField(User, blank=True,null=True)
    

class Lesson(ModelBase):
    class Meta:
        unique_together = ('subject', 'course')
    link = models.URLField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def get_id_url(self):
        parsed_url = urlparse(self.link)
        id_value = parse_qs(parsed_url.query)
        return id_value['v'][0]