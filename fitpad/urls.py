from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title= 'my swagger')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('', include('myApp.urls')),
    path('workout/', include('workout.urls')),
    path('api/', include('api.urls')),
    path('swagger/', schema_view),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)