
from django.contrib import admin
from django.urls import path, include
from .views import (
    HomePageView
)
urlpatterns = [
    path('admin/', admin.site.urls),  # localhost/admin/
    path('', HomePageView.as_view(), name='home'),
    path('book/', include('book.urls', namespace='book'))

    # namespace:name
    # name
]
