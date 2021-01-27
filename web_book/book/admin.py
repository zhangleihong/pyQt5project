from django.contrib import admin

# Register your models here.
from .models import BookInfo
# 自定义 管理类
class BookInfoAdmin(admin.ModelAdmin):
    # 列表页显示的内容
    list_display = ['id', "category", "small_category", 'name', "author", "store", "price"]


# 注册模型类  到admin站点里面去
admin.site.register(BookInfo, BookInfoAdmin)


admin.site.site_header = '传智书城'
admin.site.site_title = '传智书城MIS'
admin.site.index_title = '欢迎使用传智书城MIS'

# //*[@id="booksort"]/div[2]/dl/dt/a
# //*[@id="booksort"]/div[2]/dl/dd[1]/em/a

