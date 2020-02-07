from django.contrib import admin

from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    # 在后台管理中要展示的数据
    list_display = ('title', 'content', 'pub_time')
    # 添加过滤器
    list_filter = ('pub_time', )


admin.site.register(Article, ArticleAdmin)


