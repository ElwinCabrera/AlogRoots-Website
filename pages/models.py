from django.db import models


# Create your models here.

class Learn_Categories(models.Model):
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

    name = models.CharField(max_length=120)
    type = models.CharField(max_length=120, choices=CATEGORY_CHOICES)

    def __str__(self):
        return str(self.id)+ " - Learn Categories - "+self.name + ", "+ self.type

class Practice_Categories(models.Model):
    DATA_STRUCTURES = "DS"
    ALGORITHMS = "ALGOS"
    ADV_DATA_STRUCTURES = "DS_ADV"
    ADV_ALGORITHMS = "ALGOS_ADV"
    OTHER = "OTHER"
    # UNDEFINED = "UNDEFINED"

    CATEGORY_CHOICES = [#(UNDEFINED,"--NO CATEGORY--"),
                        (DATA_STRUCTURES, "Data Structres"), 
                        (ALGORITHMS, "Algorithms"), 
                        (ADV_ALGORITHMS,"Advanced Algorithms"), 
                        (ADV_DATA_STRUCTURES, "Advanced Data Structures"), 
                        (OTHER, "Other")]

    name = models.CharField(max_length=120)
    type = models.CharField(max_length=120, choices=CATEGORY_CHOICES)

    def __str__(self):
        return str(self.id)+ " - Practice Categories - "+self.name + ", "+ self.type


class Learn_Category_Item(models.Model):
    itemName = models.CharField(max_length=150)
    category = models.ForeignKey(Learn_Categories, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+ " - Learn Category Item - "+self.itemName 

class Practice_Category_Item(models.Model):
    itemName = models.CharField(max_length=150)
    category = models.ForeignKey(Practice_Categories, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+ " - Learn Category Item - "+self.itemName


