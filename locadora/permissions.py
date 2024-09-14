from rest_framework.permissions import BasePermission


class LocadoraOwnerPermission(BasePermission):
	def has_permission(self, request, view):
		if view.action == 'list':
			view.queryset = view.queryset.filter(owner=request.user)
			return True
		return super().has_permission(request, view)

	def has_object_permission(self, request, view, obj):
		return obj.owner == request.user or request.is_superuser == 1  # Tentativa de retornar todos os
																		# objetos para o admin sempre
