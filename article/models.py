from django.db import models
#from django.db.models.ForeignKey

# Create your models here.

class Article(models.Model):

    articleID = models.AutoField(primary_key=True)

    postDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    category = models.CharField(max_length=120, blank=True, default="!--Blank Article Category--!");
    title = models.CharField(max_length=120, blank=True, default="!--Blank Article Title--!");
    imagesPath = models.FilePathField(path="static/images/article{0}".format(articleID), blank=True ,recursive=True, max_length=100)
    preamble = models.TextField(blank=True, default="!--Blank Article Preamble--!")
    

class Section(models.Model):
    sectionId = models.AutoField(primary_key=True)
    
    title = models.CharField(max_length=120,  blank=True, default="!--Blank Section Title--!");
    secText = models.TextField( blank=True, default="!--Blank Section Text--!")
    hasSubSections = models.BooleanField(default=False)

    article = models.ForeignKey(Article,  on_delete=models.CASCADE, related_name="section")


class SubSection(models.Model):
    sectionId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120, blank=True, default="!--Blank Sub Section Title--!");
    subSecText = models.TextField( blank=True, default="!--Blank Sub Section Text--!")
    section = models.ForeignKey(Section,  on_delete=models.CASCADE, related_name="subSec", )

