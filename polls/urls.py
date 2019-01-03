from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # q_id template name must mapping to template in service level
    path('<int:pk>', views.DetailView.as_view(), name='details'),
    path('<int:q_id>/vote', views.vote, name='vote'),
]
