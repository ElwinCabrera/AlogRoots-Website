from django.db import models

# Create your models here.
class Choices():

    LEARN_ARTICLE = "LEARN_ARTI"
    PRACTICE_ARTICLE = "PRACTICE_ARTI"
    OTHER_ARTICLE = "OTHER_ARTI"
  
    ARTICLE_CHOICES = [#(UNDEFINED,"--NO CATEGORY--"),
                        (LEARN_ARTICLE, "Learn Article"), 
                        (PRACTICE_ARTICLE, "Practice Article"), 
                        (OTHER_ARTICLE,"Other"), ]

    DATA_STRUCTURES = "DS"
    ALGORITHMS = "ALGOS"
    ADV_DATA_STRUCTURES = "DS_ADV"
    ADV_ALGORITHMS = "ALGOS_ADV"
    OTHER = "OTHER"
    NONE = "NONE"
    # UNDEFINED = "UNDEFINED"

    CATEGORY_CHOICES = [#(UNDEFINED,"--NO CATEGORY--"),
                        (DATA_STRUCTURES, "Data Structres"), 
                        (ALGORITHMS, "Algorithms"), 
                        (ADV_ALGORITHMS,"Advanced Algorithms"), 
                        (ADV_DATA_STRUCTURES, "Advanced Data Structures"), 
                        (OTHER, "Other"),
                        (NONE, "NONE"),]


def articleImageUpload(instance, filename):

    if(instance.article_type == Choices.LEARN_ARTICLE):
        return 'images/articles/learn/{0}_{1}/{2}'.format(instance.category,instance.title, filename) 
    elif(instance.article_type == Choices.PRACTICE_ARTICLE):
        return 'images/articles/practice//{0}_{1}/{2}'.format(instance.category,instance.title, filename) 
    else:
        return 'images/articles/other//{0}_{1}/{2}'.format(instance.category,instance.title, filename) 




class Article(models.Model):
    

    id = models.AutoField(primary_key=True)

    post_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    article_type = models.CharField(max_length=20, choices=Choices.ARTICLE_CHOICES)
    category = models.CharField(max_length=20, choices=Choices.CATEGORY_CHOICES)
    title = models.CharField(max_length=120);
    image_upload = models.ImageField(upload_to=articleImageUpload, null=True)
    
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.id) + " - " + self.title + " ({0} Category: {1})".format(self.article_type, self.category)

    
    

class Section(models.Model):    
    title = models.CharField(max_length=120,  blank=True);
    sec_text = models.TextField(blank=True)
    has_subsections = models.BooleanField(default=False)
    gist_url = models.CharField(max_length=250, blank=True)

    article = models.ForeignKey(Article,  on_delete=models.CASCADE, related_name="section")

    def __str__(self):
        return str(self.id)+ " - "+self.title +" (In article: {0}[{1}])".format(self.article.title, self.article.id)
    


class SubSection(models.Model):
    title = models.CharField(max_length=120, blank=True);
    subsec_text = models.TextField(blank=True)
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="subSec", )
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="subSec", )
    

    def __str__(self):
        return str(self.id)+ " - "+self.title +" (In article:{0}[{1}], section: {2}[{3}])".format(self.article.title, self.article.id ,self.section.title,self.section.id)


class Strengths(models.Model):
    desc = models.CharField(max_length=120, blank=True);
    

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="Strengths")

    def __str__(self):
        return str(self.id)+ " - Strengths  (In article: {0}[{1}])".format(self.article.title, self.article.id)

class Weaknesses(models.Model):
    desc = models.CharField(max_length=120, blank=True);

    article = models.ForeignKey(Article,  on_delete=models.CASCADE, related_name="Weaknesses")

    def __str__(self):
        return str(self.id)+ " - Weaknesses (In article: {0}[{1}])".format(self.article.title, self.article.id)

class Complexity(models.Model):
    insert_best = models.CharField(max_length=20, default ="N/A", blank=True);
    insert_avg = models.CharField(max_length=20, default ="N/A", blank=True);
    insert_worst = models.CharField(max_length=20, default ="N/A", blank=True);
    
    delete_best = models.CharField(max_length=20, default ="N/A", blank=True);
    delete_avg = models.CharField(max_length=20, default ="N/A", blank=True);
    delete_worst = models.CharField(max_length=20, default ="N/A", blank=True);
    
    search_best = models.CharField(max_length=20, default ="N/A", blank=True);
    search_avg = models.CharField(max_length=20, default ="N/A", blank=True);
    search_worst = models.CharField(max_length=20, default ="N/A", blank=True);
    
    space_best = models.CharField(max_length=20, default ="N/A", blank=True);
    space_avg = models.CharField(max_length=20, default ="N/A", blank=True);
    space_worst = models.CharField(max_length=20, default ="N/A", blank=True);

    article = models.ForeignKey(Article,  on_delete=models.CASCADE, related_name="complexity")

    def __str__(self):
        return str(self.id)+ " - Complexity (In article: {0}[{1}])".format(self.article.title, self.article.id)


class ResourcesCitations(models.Model):
    source_name = models.CharField(max_length=120, blank=False)
    url = models.CharField(max_length=20, blank=False);

    article = models.ForeignKey(Article,  on_delete=models.CASCADE, related_name="resources_citations")

    def __str__(self):
        return str(self.id)+ " - Resources {0} (For article: {1}[{2}])".format(self.source_name, self.article.title, self.article.id)






class LearnCategories(models.Model):
    

    name = models.CharField(max_length=120)
    type = models.CharField(max_length=120, choices=Choices.CATEGORY_CHOICES)

    def __str__(self):
        return str(self.id)+ " - Learn Categories - "+self.name + ", "+ self.type

class PracticeCategories(models.Model):

    name = models.CharField(max_length=120)
    type = models.CharField(max_length=120, choices=Choices.CATEGORY_CHOICES)

    def __str__(self):
        return str(self.id)+ " - Practice Categories - "+self.name + ", "+ self.type


class LearnCategoryItem(models.Model):
    itemName = models.CharField(max_length=150)
    category = models.ForeignKey(LearnCategories, on_delete=models.CASCADE)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+ " - Learn Category Item - "+self.itemName 

class PracticeCategoryItem(models.Model):
    itemName = models.CharField(max_length=150)
    category = models.ForeignKey(PracticeCategories, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+ " - Learn Category Item - "+self.itemName