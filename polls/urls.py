from django.urls import path  #앱 수준의 경로 패턴 정의
from . import views

app_name = 'polls' # 앱 이름 지정

### Generic view (class-based view)
urlpatterns=[
path('', views.IndexView.as_view(), name='index'),
# ex: /polls/5/
path('<int:pk>/', views.DetailView.as_view(), name='detail'),
# ex: /polls/5/results.
path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
# ex: /polls/5/vote/
path('<int:question_id>/vote/', views.vote, name='vote'),
]