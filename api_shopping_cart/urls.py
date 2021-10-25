from django.contrib import admin
from django.urls import path,include,re_path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from apps.users.views import Login,Logout

urlpatterns = [
   path('admin/', admin.site.urls),
   path('logout/', Logout.as_view(), name = 'logout'),
   path('login/',Login.as_view(), name = 'login'),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('users/',include('apps.users.api.routers')),

]
