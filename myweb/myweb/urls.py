from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meeet_app.urls')),

]


# admin titel change
admin.site.site_header = "My Web administration"
admin.site.site_title = "Browser title"
admin.site.index_title = "Welcome to administration..."
