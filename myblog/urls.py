from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'myblog'

urlpatterns = [
    path('', login_required(views.BlogList.as_view(), login_url='accounts:login'), name="list"),
    # path('post/<slug:slug>', login_required(views.BlogDetail.as_view(), login_url='accounts:login'), name="detail"),
    path('post/<slug:slug>', login_required(views.detail_view, login_url='accounts:login'), name="detail"),
    path('create', views.create_blog, name='create')
]