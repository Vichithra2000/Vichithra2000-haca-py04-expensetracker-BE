from django.urls import path
print("LOADING EXPENSE URLS")
from .views import ExpenseCreateAPI, ExpenseListAPI,ExpenseDeleteAPI,ExpensesAioverviewAPI


urlpatterns = [
     path("api/expense/create/", ExpenseCreateAPI.as_view()),
     path("api/expense/list/", ExpenseListAPI.as_view()),
     path("api/expense/delete/", ExpenseDeleteAPI.as_view()),
     path("api/expense/ai-overview/", ExpensesAioverviewAPI.as_view()),
]