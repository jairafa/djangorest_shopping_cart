from rest_framework.routers import DefaultRouter
from apps.products.api.views.general_views import *
from apps.products.api.views.product_viewsets import ProductViewSet

router = DefaultRouter()

router.register(r'',ProductViewSet,basename = 'products')
#router.register(r'carts',CategoryProductViewSet,basename = 'category_products')

urlpatterns = router.urls