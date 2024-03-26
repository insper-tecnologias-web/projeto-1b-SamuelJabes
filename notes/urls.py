from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:note_id>/', views.delete, name='delete'),
    path('update/<int:note_id>/', views.update, name='update'),
    path('cancel/', views.cancel, name='cancel'),
    path('tags/', views.all_tags, name='all_tags'),
    path('tags/<int:tag_id>/', views.tag, name='tag'),
    path('prova/', views.prova, name='prova'),
    path('prova/<int:fact_id>', views.curtiu, name='prova'),
]