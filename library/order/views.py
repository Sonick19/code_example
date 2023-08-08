from .models import Order
from django.shortcuts import render, redirect
from book.models import Book
from datetime import datetime
from django.contrib import messages
from .forms import CreateOrderForm


def order_list(request):
    orders = Order.objects.order_by("user__id")
    return render(request, "order/order.html", {"orders": orders})


def user_orders(request):
    current_user = request.user
    orders = Order.objects.filter(user=current_user)
    return render(request, "order/user_orders.html", {"orders": orders})


def create_order(request):
    current_user = request.user
    books = Book.objects.all()

    if request.method == "POST":
        form = CreateOrderForm(request.POST)
        if form.is_valid():

            book = request.POST["book"]
            plated_end_at = request.POST["plated_end_at"]

            try:
                book = Book.objects.get(id=book)
            except Book.DoesNotExist:
                messages.error(request, "Invalid user or book.")
                return redirect("create_order")

            if book.count == 0:
                messages.error(request, "No book, you can`t order this book")

            else:
                order = Order.create(user=current_user, book=book, plated_end_at=plated_end_at)
                book.count -= 1
                book.update()
                messages.success(request, "Order created successfully.")
    else:
        form = CreateOrderForm()
    return render(
        request,
        "order/create_order.html",{'form':form}
    )


def close_order(request, order_id):
    order = Order.get_by_id(order_id)

    if order:
        order.update(end_at=datetime.now())

    return redirect("order:order")
