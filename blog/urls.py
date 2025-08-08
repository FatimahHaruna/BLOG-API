from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet

router = DefaultRouter() #this router generates all the URL path for the API automatically
router.register(r'posts', BlogPostViewSet)
#registers a route posts and connect to BlogPostViewSet

urlpatterns = [
    path('', include(router.urls)),
]
#connects API routes to your app