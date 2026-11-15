"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from myapp import views
from myproject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_books, name='show_books'),
    path('add_books', views.add_books, name='add_books'),
    path('delete_book/<int:id>', views.delete_book, name='delete_book'),
    path('edit_book/<int:id>', views.edit_book, name='edit_book'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# delete_book/1
# edit_book/10