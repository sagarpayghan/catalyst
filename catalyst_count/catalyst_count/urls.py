from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('catalyst_count_app.urls')),
    path('accounts/', include('allauth.urls')),
]


