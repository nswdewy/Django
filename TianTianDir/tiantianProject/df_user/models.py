# coding=utf-8
from django.db import models

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)#密码需要加密，预留长些
    uemail = models.CharField(max_length=30)
    uconsignee = models.CharField(max_length=20,default='')
    uplace_of_receipt = models.CharField(max_length=100,default='')
    upostcode = models.CharField(max_length=6,default='')
    uphone_number = models.CharField(max_length=11,default='')
