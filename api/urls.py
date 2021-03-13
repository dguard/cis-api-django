from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from api import settings
from graphene_django.views import GraphQLView

urlpatterns = [
    url(r'^', include('valutes.urls')),
    url(r'^', include('webhooks.urls')),
    url(r'^admin/', admin.site.urls),

    url('graphql', GraphQLView.as_view(graphiql=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
