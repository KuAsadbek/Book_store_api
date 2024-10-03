from django.db import models

class CategoryMod(models.Model):
    name = models.CharField(max_length=100,verbose_name='Category name')
    slug = models.SlugField(max_length=100,verbose_name='Category slug',unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

class GoodsMod(models.Model):
    category = models.ForeignKey(CategoryMod,on_delete=models.CASCADE,verbose_name='Product category')
    name = models.CharField(max_length=100,verbose_name='Product name')
    slug = models.SlugField(max_length=100,verbose_name='Product slug',unique=True)
    price = models.FloatField(verbose_name='Product price')
    description = models.TextField(verbose_name='Product description')
    hajmi = models.FloatField(verbose_name='Product hajmi')
    format = models.CharField(max_length=50,verbose_name='Product format')
    skid = models.IntegerField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Good'
        verbose_name_plural = 'Goods'
    
    
class PhotoGoods(models.Model):
    goods = models.ForeignKey(GoodsMod,on_delete=models.CASCADE,verbose_name='Product')
    photo = models.ImageField(upload_to='media/',verbose_name='Product photo')

    def __str__(self) -> str:
        return self.goods.name

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photo'
