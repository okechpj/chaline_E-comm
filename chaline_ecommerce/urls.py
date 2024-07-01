
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from chaline_ecommerce.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('accounts.urls')),
    path('', include('store.urls')),
   # path('', include('store.urls')),
    #path('', include('category.urls'))
] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
