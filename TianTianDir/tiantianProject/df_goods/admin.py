from django.contrib import admin
from .models import *

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'isDelete', 'ttitle']

class GoodsAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id',
                    'isDelete',
                    'gtitle',
                    'gsubtitle',
                    'gimage',
                    'gunit',
                    'gprice',
                    'ginventory',
                    'gsupplier',
                    'gpurchase_date',
                    'grecommend',
                    'gadv',
                    'gtype']

admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(Goods,GoodsAdmin)