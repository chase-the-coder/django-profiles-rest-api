from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name="hello-viewset") # base_name is required for ViewSets

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), # as_view() is required for APIView
    path('', include(router.urls)),
]