from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import redirect
from .models import Book, Contact, Profile
from .form import profileform
class HomeView(TemplateView):
    template_name = 'books/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_books'] = Book.objects.filter(is_visible=True)[:10]
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('books:home')

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(is_visible=True)

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def get_queryset(self):
        return Book.objects.filter(is_visible=True)
class myprofile(ListView):
    model = Profile
    template_name = 'books/myprofile.html'
    context_object_name = 'Profiles'
    def get_queryset(self):
        return Profile.objects.all()
class Form(TemplateView):
    template_name= 'books/form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = profileform()
        return context
    def post(self, request, *args, **kwargs):
        form = profileform(request.POST, request.FILES)
        if form.is_valid():
            # Create Team member
            profile = form.save(commit=False)
            profile.save()
            return redirect('books:home')
        return self.render_to_response(self.get_context_data(form=form))