from django.urls import path
from polls import views

#应用命名空间
app_name = 'polls'

urlpatterns = [

    # 例如: /polls/
    # path('', views.index, name='index'),

    # 例如: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    #调用：detail(request=<HttpRequest object>, question_id=34)

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # 例如: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),

    # 例如: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
