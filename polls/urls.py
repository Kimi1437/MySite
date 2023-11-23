from django.urls import path

from . import views


# 以下的这个是命名空间，为了的是项目当中如果有重名的URL地址的话，加以区分
app_name = "polls"
urlpatterns = [
    # 我在这边把各个参数都写清楚了
    path(route = "", view =views.index, name="index"),
    # 添加更过的视图，为了做测试用，注意观察这个参数的形式是怎么样的---以下
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/  多多注意里面int等方法的使用
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]