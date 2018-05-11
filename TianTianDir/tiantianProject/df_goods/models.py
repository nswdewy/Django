# coding=utf-8
from django.db import models
from tinymce.models import HTMLField

class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)# 类型名称
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle.encode('utf-8')

class Goods(models.Model):
    gnumber = models.CharField(max_length=10)# 商品编号
    gtitle = models.CharField(max_length=20)# 名称
    gsubtitle = models.CharField(max_length=100)# 副标题
    gimage = models.ImageField(upload_to='goods/')# 商品图片
    gdetail = HTMLField()# 商品介绍,图文混排
    gunit = models.CharField(max_length=20)# 单位
    gprice = models.DecimalField(max_digits=20,decimal_places=2)# 单价
    ginventory = models.IntegerField()# 库存
    gsupplier = models.CharField(max_length=20)# 供应商
    gpurchase_date = models.DateField()# 采购日期
    gseason = models.CharField(max_length=1)# 季节
    gorigin = models.CharField(max_length=20)# 产地
    gclick = models.IntegerField()# 点击量人气
    grecommend = models.IntegerField()# 推荐
    gadv = models.BooleanField(default=False)# 广告字段
    gtype = models.ForeignKey(TypeInfo)# 类型
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.gtitle.encode('utf-8')