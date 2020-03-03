from rest_framework import permissions

class IsReadOnlyOperation(permissions.BasePermission):
	def has_permission(self, request, view):
		# SAFE_METHODS = ('GET', 'OPTIONS', 'HEAD')
		if request.method in permissions.SAFE_METHODS:
			return True
		else:
			return False
