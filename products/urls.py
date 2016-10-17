from django.conf.urls import url

from products import views

urlpatterns = [
    url(r'^$', views.ProductListView.as_view(), name='list-products'),
    url(r'^add/$', views.ProductCreateView.as_view(), name='create-products'),
    url(r'^update/(?P<pk>\d+)/$', views.ProductUpdateView.as_view(), name='update-products'),
    url(r'^detail/(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='detail-products'),
    url(r'^delete/(?P<pk>\d+)/$', views.ProductDeleteView.as_view(), name='delete-products'),
    url(r'^units/$', views.UnitListView.as_view(), name='list-units'),
    url(r'^units/add/$', views.UnitCreateView.as_view(), name='create-units'),
    url(r'^units/update/(?P<pk>\d+)/$', views.UnitUpdateView.as_view(), name='update-units'),
    url(r'^units/delete/(?P<pk>\d+)/$', views.UnitDeleteView.as_view(), name='delete-units'),
]
