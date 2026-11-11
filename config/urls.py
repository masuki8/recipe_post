from django.contrib import admin
from django.urls import path, include
from lib.views import IndexTemplateView
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path("admin/", admin.site.urls),

    path('', IndexTemplateView.as_view(), name="index"),
    
    path('recipe/', include('recipe.urls')),
    path('comment/', include("comment.urls", namespace="comment")),
    path('staffroom/', include("staffroom.urls", namespace="staffroom")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
