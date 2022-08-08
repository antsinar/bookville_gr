from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('townhall/', admin.site.urls),

    path('api/',include('api.urls'))
]
