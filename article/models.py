from django.db import models
#from django.db.models.ForeignKey

# Create your models here.

class Topic(models.Model):

    articleID = models.AutoField(primary_key=True)

    postDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    category = models.CharField(max_length=120, blank=True, default="!--Blank Article Category--!");
    title = models.CharField(max_length=120, blank=True, default="!--Blank Article Title--!");
    imagesPath = models.FilePathField(path="static/images/article{0}".format(articleID), blank=True ,recursive=True, max_length=100)
    preamble = models.TextField(blank=True, default="!--Blank Article Preamble--!")

    time_worst = models.CharField(max_length=1, blank=False, default=' ')
    time_average = models.CharField(max_length=1, blank=False, default=' ')
    time_best = models.CharField(max_length=1, blank=False, default=' ')

    space_worst = models.CharField(max_length=1, blank=False, default=' ')
    space_average = models.CharField(max_length=1, blank=False, default=' ')
    space_best = models.CharField(max_length=1, blank=False, default=' ')

    def __str__(self):
        return "id: "+self.articleID + "-" + self.title 
    

class Section(models.Model):
    sectionId = models.AutoField(primary_key=True)
    
    title = models.CharField(max_length=120,  blank=True, default="!--Blank Section Title--!");
    secText = models.TextField( blank=True, default="!--Blank Section Text--!")
    hasSubSections = models.BooleanField(default=False)

    topic = models.ForeignKey(Topic,  on_delete=models.CASCADE, related_name="section")

    def __str__(self):
        return "id: "self.sectionId+ "-"self.title +"({0})".format(Topic.title)
    


class SubSection(models.Model):
    subSectionId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120, blank=True, default="!--Blank Sub Section Title--!");
    subSecText = models.TextField( blank=True, default="!--Blank Sub Section Text--!")
    section = models.ForeignKey(Section,  on_delete=models.CASCADE, related_name="subSec", )

    def __str__(self):
        return "id: "self.subSectionID+ "-"self.title +"({0})".format(Section.title)


class GoodFor(models.Model):
    item1 = models.CharField(max_length=120, blank=True, default=" ");
    item2 = models.CharField(max_length=120, blank=True, default=" ");
    item3 = models.CharField(max_length=120, blank=True, default=" ");
    item4 = models.CharField(max_length=120, blank=True, default=" ");
    item5 = models.CharField(max_length=120, blank=True, default=" ");

    topic = models.ForeignKey(Topic,  on_delete=models.CASCADE, related_name="good-for")

class NotGoodFor(models.Model):
    item1 = models.CharField(max_length=120, blank=True, default=" ");
    item2 = models.CharField(max_length=120, blank=True, default=" ");
    item3 = models.CharField(max_length=120, blank=True, default=" ");
    item4 = models.CharField(max_length=120, blank=True, default=" ");
    item5 = models.CharField(max_length=120, blank=True, default=" ");

    topic = models.ForeignKey(Topic,  on_delete=models.CASCADE, related_name="not-good-for")
    