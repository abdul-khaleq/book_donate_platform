from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from donate.models import BookDonateModel
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from comment.models import Comment
from donate.models import BookDonateModel
from comment.forms import CommentForm

class HomeListView(ListView):
    model = BookDonateModel
    template_name = 'home.html'
    context_object_name = 'books'
    # def get_queryset(self):
    #     return BookDonateModel.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] =Comment.objects.all()
        return context

class BookDetailView(DetailView):
    model = BookDonateModel
    pk_url_kwarg = 'id'
    template_name = 'book_details.html'
    context_object_name = 'book'

# @method_decorator(login_required, name='dispatch')
# class HomeAndCommentCreateView(CreateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = 'home.html'
#     success_url = reverse_lazy('homepage')

#     def get(self, request, *args, **kwargs):
#         books = BookDonateModel.objects.all()
#         comments = Comment.objects.all()
#         context = {'books': books, 'form': self.get_form(), 'comments':comments}
#         return self.render_to_response(context)
    
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
 