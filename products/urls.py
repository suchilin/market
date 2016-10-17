from django.conf.urls import url

from products import views

urlpatterns = [
    url(r'^units/$', views.UnitListView.as_view(), name='list-units'),
    url(r'^units/add/$', views.UnitCreateView.as_view(), name='create-units'),
    url(r'^units/update/(?P<pk>\d+)/$', views.UnitUpdateView.as_view(), name='update-units'),
    url(r'^units/delete/(?P<pk>\d+)/$', views.UnitDeleteView.as_view(), name='delete-units'),
]
