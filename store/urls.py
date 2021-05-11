from django.urls import path

from .views import (homeView, productDetailView, allBrandsView, userDashboardView,
                    manageProfileView, wishlistView, campaignView, flashSaleView,
                    shopwiseProductView, localShopView, searchView,
                    user_registration, user_login, logoutView,
                    categorywiseProductView, subcategorywiseProduct, brandwiseProductView)


app_name = "store"
urlpatterns = [
    path("", homeView, name="home"),
    path("product/<str:slug>/", productDetailView, name="product-detail"),
    path("brands/", allBrandsView, name="brands"),
    path("dashboard/", userDashboardView, name="dashboard"),
    path("profile/", manageProfileView, name="profile"),
    path("wishlist/", wishlistView, name="wishlist"),
    path("campaigns/", campaignView, name="campaigns"),
    path("flash-sale/", flashSaleView, name="flash-sale"),
    path("shops/<int:id>/<str:title>/", shopwiseProductView, name="shopwise-product"),
    path("categories/<int:id>/<str:title>/", categorywiseProductView, name="categorywise-product"),
    path("subcategories/<int:id>/<str:title>/", subcategorywiseProduct, name="subcategorywise-product"),
    path("brands/<int:id>/<str:title>/", brandwiseProductView, name="brandwise-product"),
    path("localshop/Mustaqeem-Localshop", localShopView, name="localshop"),
    path("search/", searchView, name="search"),

    ## Login Registration ##

    path("user_registration/", user_registration, name="user_registration"),
    path("user_login/", user_login, name="user_login"),
    path('logout/', logoutView, name='logout'),
]
