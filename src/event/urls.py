from django.urls import path
from .views import (
    event_post_detail_view,
    event_post_list_view,
    event_post_update_view,
    event_post_delete_view,
    event_post_archive_view,
    event_post_share,
)

urlpatterns = [
    path('', event_post_list_view),
    path('<str:slug>/', event_post_detail_view),
    path('<str:slug>/edit/', event_post_update_view),
    path('<str:slug>/delete/', event_post_delete_view),
    path('<str:slug>/archive/', event_post_archive_view),
    path('<str:slug>/share/', event_post_share),
]
