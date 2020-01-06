from rest_framework import routers
from .views import OrderViewSet, MotherBoardViewSet, MemoryViewSet, GraphicsCardViewSet, ProcessorViewSet


router = routers.DefaultRouter()
router.register('orders', OrderViewSet, base_name='orders')
router.register('motherboard', MotherBoardViewSet)
router.register('memory', MemoryViewSet)
router.register('gpu', GraphicsCardViewSet)
router.register('processor', ProcessorViewSet)

urlpatterns = router.urls
