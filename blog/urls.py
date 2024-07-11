from django.urls import path
from .views import blogListView, blogCreateView, blogDetailView

app_name="blog"

urlpatterns = [
    path('', blogListView.as_view(), name="Home"),
    path('create/', blogCreateView.as_view(), name="Create"),
    path('<int:pk>', blogDetailView.as_view(), name="Detail"),
]