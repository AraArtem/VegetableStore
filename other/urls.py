from django.urls import path


from .views import CurrentDateView


urlpatterns = [
   path('datetime/', CurrentDateView.as_view()),
]

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
   path('admin/', admin.site.urls),
   path('other/', include('other.urls')),
]

