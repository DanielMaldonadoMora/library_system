from rest_framework.routers import DefaultRouter
from library.api.views import LibraryApiViewSet,RackApiViewSet

router_library = DefaultRouter()


router_library.register(prefix='library', basename='library', viewset=LibraryApiViewSet)
router_library.register(prefix='library/racks', basename='racks', viewset=RackApiViewSet)