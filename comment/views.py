from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Comment
from .forms import CommentForm

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] =Comment.objects.all()
        context['type'] = 'Review'
        context['button_text'] = 'Review'
        context['icon'] = 'fa-regular fa-comment-dots text-info'
        context['has_account'] = "Return "
        context['redirect'] = "homepage"
        context['user_to_another'] = "home"
        return context