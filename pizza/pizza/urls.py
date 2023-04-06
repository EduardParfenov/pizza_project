"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Добавляем элемент catalog в список urlpatterns, который направляет запросы с адреса catalog/ к catalog.urls
from django.urls import include
from django.urls import path

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

# Перенаправление корневого URL на .../catalog/
from django.views.generic import RedirectView

urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

# Размещение статических файлов (CSS, JavaScript и изображений)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# подключаем аутентификацию пользователя
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
