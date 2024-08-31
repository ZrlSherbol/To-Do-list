from django.contrib import admin
from django.urls import path
from tasks.views import ListView, main_view, CreateView, DatailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('tasks/', ListView),
    path('tasks/<int:post_id>/', DatailView),
    path('task_create/', CreateView)
]
