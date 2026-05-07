from .import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.page1,name='page1'),
    path('Reservation/',views.Reservation,name='page2')
] 
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

