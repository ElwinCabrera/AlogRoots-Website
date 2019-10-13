from django.db import models
#from django.db.models.ForeignKey

# Create your models here.


class Article(models.Model):
    DATA_STRUCTURES = "DS"
    ALGORITHMS = "ALGOS"
    ADV_DATA_STRUCTURES = "DS_ADV"
    ADV_ALGORITHMS = "ALGOS_ADV"
    OTHER = "OTHER"
    UNDEFINED = "UNDEFINED"

    CATEGORY_CHOICES = [(UNDEFINED,"--NO CATEGORY--"),
                        (DATA_STRUCTURES, "Data Structres"), 
                        (ALGORITHMS, "Algorithms"), 
                        (ADV_ALGORITHMS,"Advanced Algorithms"), 
                        (ADV_DATA_STRUCTURES, "Advanced Data Structures"), 
                        (OTHER, "Other")]

    id = models.AutoField(primary_key=True)

    post_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=120);
    images_path = models.FilePathField(path="static/images/article{0}".format(title), blank=True ,recursive=True, max_length=100)
    
    description = models.TextField(blank=True)

    time_worst = models.CharField(max_length=4, blank=True)
    time_average = models.CharField(max_length=4,blank=True)
    time_best = models.CharField(max_length=4,blank=True)

    space_worst = models.CharField(max_length=4,blank=True)
    space_average = models.CharField(max_length=4,blank=True)
    space_best = models.CharField(max_length=4,blank=True)

    

    def __str__(self):
        return str(self.id) + " - " + self.title + " (Category: {0})".format(self.category) 
    

class Section(models.Model):    
    title = models.CharField(max_length=120,  blank=True);
    sec_text = models.TextField(blank=True)
    has_subsections = models.BooleanField(default=False)

    article = models.ForeignKey(Article,  on_delete=models.CASCADE, related_name="section")

    def __str__(self):
        return str(self.id)+ " - "+self.title +" (In article: {0}[{1}])".format(self.article.title, self.article.id)
    


class SubSection(models.Model):
    title = models.CharField(max_length=120, blank=True);
    subsec_text = models.TextField(blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="subSec", )
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="subSec", )

    def __str__(self):
        return str(self.id)+ " - "+self.title +" (In article:{0}[{1}], section: {2}[{3}])".format(self.article.title, self.article.id ,self.section.title,self.section.id)


class GoodFor(models.Model):
    item1 = models.CharField(max_length=120, blank=True, default=" ");
    item2 = models.CharField(max_length=120, blank=True, default=" ");
    item3 = models.CharField(max_length=120, blank=True, default=" ");
    item4 = models.CharField(max_length=120, blank=True, default=" ");
    item5 = models.CharField(max_length=120, blank=True, default=" ");

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="goodFor")

class NotGoodFor(models.Model):
    item1 = models.CharField(max_length=120, blank=True, default=" ");
    item2 = models.CharField(max_length=120, blank=True, default=" ");
    item3 = models.CharField(max_length=120, blank=True, default=" ");
    item4 = models.CharField(max_length=120, blank=True, default=" ");
    item5 = models.CharField(max_length=120, blank=True, default=" ");

    article = models.ForeignKey(Article,  on_delete=models.CASCADE, related_name="notGoodFor")
    