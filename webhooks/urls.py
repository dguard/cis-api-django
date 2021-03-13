from django.urls import include, path, re_path
from . import views


urlpatterns = [
    re_path(r'^api/v1/webhooks/(?P<pk>[0-9]+)$',
        views.get_delete_update_webhook.as_view(),
        name='get_delete_update_webhook'
    ),
    path('api/v1/webhooks/',
        views.get_post_webhooks.as_view(),
        name='get_post_webhooks'
    )
]
