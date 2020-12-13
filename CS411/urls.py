from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# from django.views.generic import TemplateView # Chew 

from django.contrib.auth.views import auth_logout # Lamas

# urlpatterns = [
#     path('admin', admin.site.urls),
#     #path('', include('main.urls')),
#     path('', include('social_django.urls', namespace = 'social')),
#     path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# # below added from Chew ??
# urlpatterns = [
#     path('', TemplateView.as_view(template_name='templates/index.html')), # 'loginapp/index/index.html'
#     path('admin/', admin.site.urls),
#     path('accounts/', include('allauth.urls')),
# ]


# Lamas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('social_django.urls', namespace = 'social')),
    path('logout/', auth_logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]
