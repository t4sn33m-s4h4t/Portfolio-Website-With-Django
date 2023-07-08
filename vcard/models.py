from django.db import models

from django.utils.text import slugify
class Home(models.Model):
    name = models.CharField(max_length=100)
    
    short_intro = models.TextField()
    
    image = models.ImageField(upload_to='profile_images')
    cv = models.FileField(upload_to='cvs')
    def __str__(self):
        return self.name
    
class About(models.Model):
    about_image = models.ImageField(upload_to='about/images')
    projects_completed = models.IntegerField(default=0)
    years_of_experience = models.IntegerField(default=0)
    happy_clients = models.IntegerField(default=0)
    customer_reviews = models.IntegerField(default=0)


class Skill(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField(default=50)
    

    def __str__(self):
        return self.name
class Education(models.Model):
    starting_year = models.IntegerField()
    finished_year = models.CharField(max_length=255, default='Present')
    title = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Portfolio(models.Model):
    portfolio_image = models.ImageField(upload_to='portfolio/images')
    github_repo_link = models.CharField(max_length=500)
    title = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.title




class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    featured_image = models.ImageField(upload_to='blog/images', null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Social(models.Model):
    media_link = models.URLField(max_length=255)
    media_icon = models.CharField(max_length=100, default='fab fa-facebook-f')

    def __str__(self):
        return self.media_link
class Contact_Details(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
