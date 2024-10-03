from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories',views.CategoryListCreate)
router.register(r'goods', views.GoodsViewSet)
router.register(r'photo', views.ProductList)


urlpatterns = [
    path('', include(router.urls)),
]