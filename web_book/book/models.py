from django.db import models

# Create your models here.
class BookInfo(models.Model):

    # 2.定义字段  属性
    category = models.CharField(max_length=50, default="大类", verbose_name="图书大类")
    small_category = models.CharField(max_length=50, default="小类", verbose_name="图书小分类")
    name = models.CharField(max_length=100, default="无", verbose_name="书名")
    author = models.CharField(max_length=50, default="无", verbose_name="作者")
    store = models.CharField(max_length=100, default="无", verbose_name="出版社")
    price = models.DecimalField(decimal_places=2, max_digits=10, default="0.00", verbose_name="价格")
    default_image = models.ImageField(null=True, verbose_name="图片")

    class Meta:
        verbose_name = "图书"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
