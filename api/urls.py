from api.views import UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
urlpatterns = [

]
urlpatterns += router.urls