from django.urls import path, include
from applications.product.views import CategoryViewSet, ProductViewSet, FavoriteViewSet, CommentViewSet
from applications.file.views import FileViewSet
from rest_framework.routers import DefaultRouter
from applications.order.views import OrderConfirm
from applications.order.models import Order
from applications.order.views import OrderViewSet


router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('comment', CommentViewSet)
router.register('favorite', FavoriteViewSet)
router.register('file', FileViewSet)
router.register('order', OrderViewSet)
router.register('', ProductViewSet)


urlpatterns = [
    path('order/activate/<uuid:confirm_code>/', OrderConfirm.as_view()),
]

urlpatterns += router.urls