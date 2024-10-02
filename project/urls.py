from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  # Para configurar os arquivos estáticos nas urls
from django.conf import settings  # Usa toda vez que precisar importar alguma coisa de settings e É MAIS RECOMEDÁVEL

#  from project import settings daria no mesmo, mas outro é mais recomendável


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls'))
]

# configurar a entrega de arquivos estáticos e de mídia no Django
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Concatena urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Concatena urls
