# """
# URL configuration for investments project - portfolio app.
# """
# from django.urls import path
# from portfolio import views
#
# urlpatterns = [
#     path('', views.customer_list),
#     path('api/customers/', views.customer_list),
#     path('api/mycustomers/', views.my_customer_list),
#     path('api/customers/<int:pk>', views.getCustomer),
#     path('api/investments/', views.investment_list),
#     path('api/investments/<int:pk>', views.getInvestment),
#     path('api/stocks/', views.stock_list),
#     path('api/stocks/<int:pk>', views.getStock),
# ]

from django.urls import path, include
from . import views

urlpatterns = [
    # Reader URLs
    path('', views.reader_list),
    path('api-auth', include('rest_framework.urls')),
    path('api/readers/', views.reader_list, name='reader-list'),
    path('api/readers/<int:pk>/', views.getReader, name='reader-detail'),
    path('api/books/', views.book_list, name='book-list'),
    path('api/books/<int:pk>/', views.getBook, name='book-detail'),
    path('api/authors/', views.author_list, name='author-list'),
    path('api/authors/<int:pk>/', views.getAuthor, name='author-detail'),
    path('api/reviews/', views.review_list, name='review-list'),
    path('api/reviews/<int:pk>/', views.getReview, name='review-detail'),
    path('api/book-buddies/', views.book_buddy_list, name='book-buddy-list'),
    path('api/book-buddies/<int:pk>/', views.getBookBuddy, name='book-buddy-detail'),
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/user/', views.getUser, name='user-detail'),
]
