# from actual_polls.views import index, index_render
from django.urls import path
from . import views
app_name = "polls"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('no_render/', index, name='index_no_render'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
