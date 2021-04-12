from django.contrib import admin
from django.urls import path, include
from .views import redirect_blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', redirect_blog)

]
