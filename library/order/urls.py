from django.urls import path
from . import views
from utils import deny_non_librarian

app_name = "order"

urlpatterns = [
    path("", deny_non_librarian(views.order_list), name="order"),
    path("create/", (views.create_order), name="create_order"),
    path("user/", (views.user_orders), name="user_orders"),
    path("close/<int:order_id>/", (views.close_order), name="close_order"),
]
