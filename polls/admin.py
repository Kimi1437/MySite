from django.contrib import admin

from .models import Choice, Question

# 向管理页面中加入投票应用,我们得告诉管理，问题 Question 对象需要一个后台接口
admin.site.register(Question)
admin.site.register(Choice)