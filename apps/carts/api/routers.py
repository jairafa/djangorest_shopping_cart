from rest_framework.routers import DefaultRouter
from apps.carts.api.views.cart_viewsets import *
#from apps.carts.api.views.cart_item_viewsets import *
#from apps.carts.api.views.inventory_viewsets import *


router = DefaultRouter()

router.register(r'',CartViewSet,basename = 'carts')
#router.register(r'carts',CategoryProductViewSet,basename = 'category_products')

urlpatterns = router.urls