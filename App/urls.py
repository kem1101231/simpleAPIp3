from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies, name="Movies"), 
    path('<int:movie_id>/details/', views.getMovieDetails, name="Movie Details"), 
    path('test/', views.funtest, name="Func"), 
    path('add_movie/', views.addMovie, name="Add Movie"),

    # ===========================================================
    # Simple POS Function URLs

    path('products/', views.getAllProducts, name="Products"),
    path('product/<int:reference_id>/details/', views.getProductDetails, name="Product Details"), 
    path('product/add/', views.addProduct, name="Add Product"),

    path('suppliers/', views.getAllSuppliers, name="Suppliers"),
    path('supplier/<int:reference_id>/details/', views.getSupplierDetails, name="Supplier Details"), 
    path('supplier/add/', views.addSupplier, name="Add Supplier"),


    path('purchases/', views.getAllPurchase, name="Purchase"),
    path('purchase/<int:reference_id>/details/', views.getPurchaseDetails, name="Purchase Details"), 
    path('purchase/add/', views.addPurchase, name="Add Purchase"),

]
