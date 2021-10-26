from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('dashboard/', views.home, name="home"),
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

	path('login/', views.loginPage, name="login"),  
	path('register/', views.registerPage, name="register"),
	path('logout/', views.logoutUser, name="logout"),
	path('product/', views.product, name="product"),
	path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
	path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
	path('item_order/<str:pk>/', views.itemOrder, name="item_order"),

	path('update_dash/<str:pk>/', views.updatecustomerDash, name="update_prof"),
	path('delete_dash/<str:pk>/', views.deletecustomerDash, name="delete_prof"),




]