from django.db import models


# Create your models here.

class Learn_Categories(models.Model):
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


class Learn_Category_Item(models.Model):
    itemName = models.CharField(max_length=150)
    category = models.ForeignKey(Learn_Categories, on_delete=models.CASCADE)

class Practice_Category_Item(models.Model):
    itemName = models.CharField(max_length=150)
    category = models.ForeignKey(Practice_Categories, on_delete=models.CASCADE)


