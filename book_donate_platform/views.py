from django.views.generic import ListView
from donate.models import BookDonateModel
from comment.models import Comment
from donate.models import BookDonateModel

class HomeListView(ListView):
    model = BookDonateModel
    template_name = 'home.html'
    context_object_name = 'books'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] =Comment.objects.all()
        return context
 