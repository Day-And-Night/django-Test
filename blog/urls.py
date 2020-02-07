from django.urls import path

from . import views

app_name = '[blog]'


'''
   此处有瑕疵，应当使用正则表达式来严格约束域名，（域名跳转如果遇到符合的就会跳转，比如：如果edit/<article_id>在edit/action之前，输入edit/action域名，
   会优先跳转进edit/<article_id>中,所以要十分注意，所以交换两个顺序。）-
'''
urlpatterns = [
    path('', views.index),
    path('article/<article_id>', views.article_page, name='article_page'),
    path('edit/action', views.edit_action, name="edit_action"),
    path('edit/<article_id>', views.edit_page, name="edit_page"),

]
