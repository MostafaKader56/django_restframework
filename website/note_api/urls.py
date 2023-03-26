from django.urls import path
from note_api.views import *
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register('notes', NoteViewSet, basename='notes')

urlpatterns = [
    # path('<str:nickname>/', name),
    path('', showAll),
    # path('<int:id>/', showOne),
    path('asd/', createOne),
    path('json/', responseWithJason),
    path('api/', getNotes),
    path('api/<int:id>', getNote),
    path('api/create', createNote),
    path('api/<int:idInput>/update', updateNote),
    path('api/<int:idInput>/delete', deleteNote),
    path('apis/', include(router.urls))
]
