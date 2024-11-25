from django.urls import path
from .views import (
    NewsList, NewDetail, NewCreate, NewUpdate, NewDelete
)


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', NewsList.as_view(), name='new_list'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:id>', NewDetail.as_view(), name='new_detail'),
   path('create/', NewCreate.as_view(), name='new_create'),
   path('<int:pk>/edit/', NewUpdate.as_view(), name='new_edit'),
   path('<int:pk>/delete/', NewDelete.as_view(), name='new_delete')

]