from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt import views as jwt_views

schema_view = get_schema_view(
    openapi.Info(
        title="Sepris API",
        default_version='v1',
        description="Tnis is an evaluation test app",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="p.barjoueian@gmail.com"),
        license=openapi.License(name="GNU License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
                                           cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),    url(r'^admin/', admin.site.urls),
    path('api/account/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/account/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/', include('account.urls')),
    path('api/', include('libman.urls')),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
