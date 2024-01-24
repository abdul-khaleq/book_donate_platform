
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.HomeView.as_view(), name='homepage'),
    path('', views.HomeAndCommentCreateView.as_view(), name='homepage'),
    path('detail/<int:id>', views.BookDetailView.as_view(), name='book_details'),
    path('user/', include('user.urls')),
    path('donate/', include('donate.urls')),
    path('comment/', include('comment.urls')),
    path('gift/', include('gift.urls')),
    path('about_us/', include('about_us.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
