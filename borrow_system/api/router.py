from rest_framework.routers import DefaultRouter
from borrow_system.api.views import BorrowApiViewSet

router_borrows = DefaultRouter()


router_borrows.register(prefix='borrow', basename='borrow', viewset=BorrowApiViewSet)