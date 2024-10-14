from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib import messages
from django.views.generic import UpdateView
from django.shortcuts import redirect

@login_required()
def Main_page(request):
    return render(request, 'main.html')

'''
View to create a new Book entry.
Requires the user to be logged in to access this view.
Check If the form is valid or Invalid and Redirect back to the book creation form

'''
class BookCreateView(LoginRequiredMixin,CreateView):
    model = Book
    fields = ['title', 'is_borrowed', 'category', 'publication_date', 'author']
    template_name = 'create_Book.html'
    permission_classes = [IsAuthenticated]

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Book {} was created successfully.'.format(form.cleaned_data['title']))
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'There was an error creating the Book. Try again . Book name must be Unique')
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse('create_Book')
    

'''
View to list and filter books based on title and category queries.
Requires the user to be logged in to access this view.
Prepare the context for rendering based on user role (superuser or regular user)
'''
@login_required()
def list(request):
    queryset = Book.objects.all()
    name_query  = request.GET.get('title')
    category_query = request.GET.get('category')

    if name_query:
        queryset = queryset.filter(title__icontains=name_query)
    if category_query:
        queryset = queryset.filter(category__icontains=category_query)
    if str(name_query).lower() == 'all' and request.user.is_superuser:
        queryset = Book.objects.all()
    serializer = bookSerializer(queryset, many=True)
    context = {'Books': serializer.data,}
    if not request.user.is_superuser and not name_query and not category_query:
        context = {'Books': ''}
    return render(request,'view_all_Books.html',context)



'''
View to update the borrow status of a book. 
Requires the user to be logged in and have admin permissions.
'''
class BookBorrowUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['is_borrowed']
    permission_classes = [IsAdminUser]
    template_name = 'update_borrow_status.html'
    
    def form_valid(self, form):
        book = form.save(commit=False)
        book.is_borrowed = form.cleaned_data['is_borrowed']
        book.save()
        messages.success(self.request, f"Book '{book.title}' borrow status was updated successfully.")
        return redirect('view_all_fun')

    def form_invalid(self, form):
        messages.error(self.request, f"There was an error updating the borrow status for '{form.instance.title}'. Please try again.")
        return super().form_invalid(form)

    def get_success_url(self):
        return redirect('view_all_fun')
    
    

# class BookDeleteView(LoginRequiredMixin, DeleteView):
#     model = Book
#     template_name = 'Delete.html'
#     success_url = redirect('view_all_fun')  # Redirect to the list view after deletion

#     # Only allow superusers to delete books
#     def test_func(self):
#         return self.request.user.is_superuser

#     def delete(self, request, *args, **kwargs):
#         book = self.get_object()
#         messages.success(self.request, f"Book '{book.title}' was deleted successfully.")
#         return super().delete(request, *args, **kwargs)