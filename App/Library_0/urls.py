from django.urls import path
from Library_0.views import *
from Library_0 import views


urlpatterns = [
    path('',views.Main_page, name = 'homeclinic'),
    path('Create_Book/', BookCreateView.as_view(), name= 'create_Book'),
    path('all/',list,name = 'view_all_fun'),
    path('book/<int:pk>/update_borrow_status/', BookBorrowUpdateView.as_view(), name='update_borrow_status'),

]