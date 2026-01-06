from django.urls import path
from access_control import views as access_control_views




urlpatterns = [
     path('logs/', access_control_views.AccessLogListCreateView.as_view(), name='access-log-list'),
     path('logs/<int:pk>/', access_control_views.AccessLogRetrieveUpdateDestroyView.as_view(), name='access-log-detail'),
]
