from django.urls import path,include
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register('hero',views.HeroViewSet)
router.register('heroine',views.HeroineViewSet)
urlpatterns = [
    path('',include(router.urls)),
]
