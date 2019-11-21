from django.urls import path
from .views import (
    event_post_detail_view,
    event_post_list_view,
    event_post_update_view,
    event_post_delete_view,
)

urlpatterns = [
    path('', event_post_list_view),
    path('<str:slug>/', event_post_detail_view),
    path('<str:slug>/edit/', event_post_update_view),
    path('<str:slug>/delete/', event_post_delete_view),
]