from rest_framework import routers
from django.urls import path
from todos import views
# from .views import TodoViewSet

# router = routers.DefaultRouter()
# router.register(r'api/todos', TodoViewSet, 'todos')

# urlpatterns = router.urls

urlpatterns = [
    path('',  views.getData),
    path('add', views.addData),
    path('update/<id>', views.updateData),
    path('delete/<id>', views.deleteData)
]

