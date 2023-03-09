from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin, DeleteView

from .utils import *
from .models import *
from .forms import *


class HomeShow(DataMixin, ListView):
    model = Book
    template_name = 'bookshop/home.html'
    context_object_name = 'books'
    extra_context = {'title': 'Bookshop',
                     'genre_selected': 0}

    def get_queryset(self):
        return Book.objects.filter(in_stock=True).select_related('genre')


class SupportFormView(DataMixin, FormView):
    form_class = SupportForm
    template_name = 'bookshop/support.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Поддержка")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class ShowBook(FormMixin, DetailView):
    model = Book
    template_name = 'bookshop/book.html'
    slug_url_kwarg = 'book_slug'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.book = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('book', kwargs={'book_slug': self.get_object().slug})


class BooksGenre(DataMixin, ListView):
    model = Book
    template_name = 'bookshop/home.html'
    context_object_name = 'books'
    allow_empty = False

    def get_queryset(self):
        return Book.objects.filter(in_stock=True, genre__slug=self.kwargs['genre_slug']).select_related('genre')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def pageNotFound(reuqest, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


class Order(LoginRequiredMixin, CreateView):
    form_class = Cart
    template_name = 'bookshop/new_supply.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заказ'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'bookshop/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'bookshop/login.html'

    def get_user_context(self, *, object_list=None, **kwargs):
        context = super().get_user_context(**kwargs)
        c_def = self.get_context_data(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class RePassword(DataMixin, RePassword):
    template_name = 'bookshop/re_login.html'

    def get_success_url(self):
        return reverse_lazy('reset_password')


class ResetPassword(DataMixin, ResetPassword):
    template_name = 'bookshop/reset_password.html'

    def get_success_url(self):
        return reverse_lazy('home')


def ShowProfile(request):
    return render(request, template_name='bookshop/profile.html')


class ShowProfileOrder(DataMixin, ListView):
    model = Chek
    template_name = 'bookshop/my_order.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Chek.objects.filter(user__pk=self.request.user.pk).select_related('user')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ShowProfileComments(DataMixin, ListView):
    model = Comment
    template_name = 'bookshop/my_comment.html'
    context_object_name = 'comments'

    def get_queryset(self):
        return Comment.objects.filter(author__pk=self.request.user.pk).select_related('author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
