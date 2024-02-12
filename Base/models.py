from django.db import models


# This Class is for store category details.
class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='uploads', default='default_value')

    def __str__(self):
        return self.name


# This Class is for store sub_category details.
class Sub_category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    sub_name = models.CharField(max_length=50, blank=False, null=False)
    S_image = models.ImageField(upload_to='uploads', default='default_value')

    def __str__(self):
        return self.sub_name


# This Class is for store products details.

class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    sub_category = models.ForeignKey(Sub_category, on_delete=models.CASCADE, null=True)
    p_name = models.CharField(max_length=50)
    p_image = models.ImageField(upload_to='uploads', default='default_value')

    def __str__(self):
        return self.p_name

