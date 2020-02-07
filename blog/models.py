from django.db import models


class Article(models.Model):
    # 数据库
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(auto_now=True, null=True)

    # 使管理页面展示文章题目
    def __str__(self):
        return self.title
