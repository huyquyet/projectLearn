# Create your views here.
from django.contrib.auth.decorators import user_passes_test

requirement_admin = user_passes_test(lambda u: u.is_staff, login_url='fels:login-admin')


# Course
@requirement_admin
def admin_delete_course(request):
    pass
