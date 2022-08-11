from rest_framework.permissions import BasePermission
from borrow_system.models import Borrow
#from comments.models import Comment


class PermissionBorrowView(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            id_borrow = view.kwargs['pk']
            borrow = Borrow.objects.get(pk=id_comment)
            id_user_borrow = borrow.user_id
            #Obtener el id del  usuario que solicita el cambio
            id_user = request.user.pk
            #Si es el mismo, pasa
            if id_user == id_user_borrow or request.user.status=="librarian":
                return True
        elif  request.user.status=="librarian":
            return True
    