from functools import wraps
from flask import abort
from flask_login import current_user

def permission_required(permission):
	def decoretor(f):
		@wraps
		def decorated_function(*args, **kwargs):
			if not current_user.can(permission):
				abort(403)
				return f(*args, *kargs)
		return decorated_function
	return decorator
	
def admin_required(f):
	return permission_required(Permission.ADMINSTER)(f)