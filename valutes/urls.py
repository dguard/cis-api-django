from django.urls import include, path, re_path
from . import views


urlpatterns = [
    re_path(r'^api/v1/valutes/(?P<pk>[0-9]+)$',
        views.get_valute.as_view(),
        name='get_valute'
    ),
    path('api/v1/valutes/',
        views.get_valutes.as_view(),
        name='get_valutes'
    )
]
