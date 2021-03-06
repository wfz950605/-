from django.contrib import admin
from .models import TypeInfo,GoodsInfo


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']
class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','gtitle','gprice','gunit','gclick','gjianjie','gkucun','gcontent','gtype']


admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)