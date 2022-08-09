from rest_framework.permissions import BasePermission
#from comments.models import Comment


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method=='POST':
            if request.user.status=="librarian":
                return True 
            return False
    