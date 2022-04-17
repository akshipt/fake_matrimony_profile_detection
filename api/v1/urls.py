from django.urls import path, include

urlpatterns = [
    path('adminuser/', include('api.v1.adminuser.urls'))
]
