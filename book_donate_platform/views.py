from django.views.generic import ListView
from donate.models import BookDonateModel
from django.shortcuts import render


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from comment.models import Comment
from comment.forms import CommentForm

# class HomeView(ListView):
#     model = BookDonateModel
#     template_name = 'home.html'
#     context_object_name = 'books'
#     def get_queryset(self):
#         return BookDonateModel.objects.all()

# @method_decorator(login_required, name='dispatch')
class HomeAndCommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'home.html'
    success_url = reverse_lazy('homepage')

    def get(self, request, *args, **kwargs):
        books = BookDonateModel.objects.all()
        comments = Comment.objects.all()
        context = {'books': books, 'form': self.get_form(), 'comments':comments}
        return self.render_to_response(context)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
 