from main.views.verif_code_view import VerifCodeView
from main.views.deal_view import DealListView
from main.models.deal import Deal
from django.urls import path
import main.views as views

app_name = 'main'

urlpatterns = [
    path('user/', views.UserView.as_view()),
    path('userIndivid/', views.IndividualView.as_view()),
    path("verifCode/", views.VerifCodeView.as_view()),
    path('userEntity/', views.EntityView.as_view()),
    path('userUpdateIndivid/<int:pk>/', views.IndividualUpdateView.as_view()),
    path('userUpdateEntity/<int:pk>/', views.EntityUpdateView.as_view()),
    path("products/", views.ProductsView.as_view()),
    path("deal/", views.DealCreateView.as_view()),
    path("deals/",views.DealListView.as_view()),
    path("transactions/", views.TransactionListView.as_view()),
    path("news/",views.NewsListView.as_view()),
    path("newsPreview/",views.NewsPreviewList.as_view()),
    path("newsItem/<int:pk>/", views.NewsItemView.as_view()),
    path("userDeposite/",views.DepositView.as_view()),
    path("items/",views.ItemsView.as_view())
]