from django.db import models
#from django.db.models.ForeignKey

# Create your models here.

class Article(models.Model):

    articleID = models.AutoField(primary_key=True)

    postDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    category = models.CharField(max_length=120);
    title = models.CharField(max_length=120);
    imagesPath = models.FilePathField(path="/static/images/article{0}".format(articleID), match='*.*', recursive=True, max_length=100)
    preamble = models.TextField()
    

class Section(models.Model):
    sectionId = models.AutoField(primary_key=True)
    
    title = models.CharField(max_length=120);
    secText = models.TextField()
    hasSubSections = models.BooleanField(default=False)

    article = models.ForeignKey(Article,  on_delete=models.CASCADE, related_name="section")


class SubSection(models.Model):
    sectionId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120);
    subSecText = models.TextField()
    section = models.ForeignKey(Section,  on_delete=models.CASCADE, related_name="subSec")

