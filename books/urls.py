from django.urls import path
from django.contrib.auth import views as auth_views
from .views import BookCategoryListView, BookCategoryCreateView, BookCategoryUpdateView, BookCategoryDeleteView, BookListView, BookCreateView, BookUpdateView, BookDeleteView, ImportDataView, UserLogoutView, app_summary, expense_report, signup_view

urlpatterns = [
    path('categories/', BookCategoryListView.as_view(), name='bookcategory_list'),
    path('categories/create/', BookCategoryCreateView.as_view(), name='bookcategory_create'),
    path('categories/<int:pk>/update/', BookCategoryUpdateView.as_view(), name='bookcategory_update'),
    path('categories/<int:pk>/delete/', BookCategoryDeleteView.as_view(), name='bookcategory_delete'),

    path('books/', BookListView.as_view(), name='book_list'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),

    path('import/', ImportDataView.as_view(), name='import_data'),

    path('expense_report/', expense_report, name='expense_report'),

    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('logout_page/', UserLogoutView, name="logout_page"),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    
    path('signup/', signup_view, name='signup'),

    path('app-summary/', app_summary, name='dashboard'),
]
