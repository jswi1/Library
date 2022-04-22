from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = {
    path('admin/', admin.site.urls),
    path('', salomlash),
    path('/men', men),
    path('asosiy/', asosiy),
    path('loyiha/', loyiha),
    path('kitoblar/', kitoblar),
    path('students/', students),
    path('muallif-t/<int:pk>/', muallif_edit),
    path('kitoblar/<int:op>/', books_edit),
    path('Kitob/<int:son>', kitob_ochir),
    path('Student/<int:son>', st_ochir),
    path('Muallif/<int:son>', mlf_ochir),
    path('/Record', recordlar),
}
