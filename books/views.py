from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BookCategory, Book
from .forms import BookForm
from django.views import View
import pandas as pd
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.urls.base import reverse
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponseRedirect
from django.utils.http import urlsafe_base64_decode


# Book Category Views
class BookCategoryListView(ListView):
    model = BookCategory
    template_name = 'book_category/bookcategory_list.html' 

class BookCategoryCreateView(CreateView):
    model = BookCategory
    template_name = 'book_category/bookcategory_form.html'  
    fields = ['name']

class BookCategoryUpdateView(UpdateView):
    model = BookCategory
    template_name = 'book_category/bookcategory_form.html'  
    fields = ['name']

class BookCategoryDeleteView(DeleteView):
    model = BookCategory
    template_name = 'book_category/bookcategory_confirm_delete.html' 
    success_url = reverse_lazy('bookcategory_list')  

# Book Views
class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book_form.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book_form.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')


class ImportDataView(View):
    template_name = 'extra/import_data.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if 'file' in request.FILES:
            file = request.FILES['file']
            if file.name.endswith('.xlsx'):
                try:
                    df = pd.read_excel(file)

                    with transaction.atomic():
                        for index, row in df.iterrows():
                            book_data = {
                                'title': row['title'],
                                'subtitle': row['subtitle'],
                                'author': row['author'],
                                'publishing_date': row['publishing_date'],
                                'publisher': row['publisher'],
                                'category': row['category'],
                                'distribution_expenses': row['distribution_expenses'],
                            }

                            form = BookForm(book_data)
                            if form.is_valid():
                                form.save(commit=False)
                                form.instance.id = None
                                form.save()
                            else:
                                print(f"Validation errors for row {index + 2}: {form.errors.as_data()}")

                    return redirect('book/book_list')
                except pd.errors.ParserError:
                    # Handle parsing errors if the spreadsheet format is incorrect
                    pass

        return render(request, self.template_name)


def expense_report(request):
    categories = BookCategory.objects.all()
    category_expenses = []

    for category in categories:
        category_books = Book.objects.filter(category=category)
        total_expense = sum(book.distribution_expenses for book in category_books)
        category_expenses.append({'category': category, 'total_expense': total_expense})

    context = {'category_expenses': category_expenses}
    return render(request, 'extra/expense_report.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})\
    

def UserLogoutView(request):
    return render(request, "registration/logout.html")


def app_summary(request):
    num_categories = BookCategory.objects.count()
    num_books = Book.objects.count()

    context = {
        'num_categories': num_categories,
        'num_books': num_books,
    }

    return render(request, 'extra/app_summary.html', context)



def password_reset_confirm_view(request, uidb64, token):
    # Decode uidb64 to get the user object
    try:
        uid = urlsafe_base64_decode(uidb64).decode('utf-8')
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your password has been reset successfully. You can now log in with your new password.')
                return HttpResponseRedirect(reverse('registration/login'))
        else:
            form = SetPasswordForm(user)

        context = {
            'form': form,
            'uid': uidb64,
            'token': token,
        }
        return render(request, 'registration/password_reset_confirm.html', context)
    else:
        messages.error(request, 'The password reset link is invalid or has expired.')
        return HttpResponseRedirect(reverse('password_reset'))