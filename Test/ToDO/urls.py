from django.urls import path
from . import views
urlpatterns = [
    path('',views.item_to_do),
    path('list/',views.list_of_item,name="lists"),
    path('deleted/<int:todo_id>/',views.todo_done,name="done"),
]