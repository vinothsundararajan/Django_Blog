from django.urls import path , include
from .views import HomeView, EntryView, CreateEntryView
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve


urlpatterns = [
    #path('home/', HomeView.as_view(), name = 'blog-home')
    path('', HomeView.as_view(), name = 'blog-home'),
    path ('entry/<int:pk>/', EntryView.as_view(), name = "entry-detail"),
    path ('create_entry/', CreateEntryView.as_view(success_url="/"), name = "create_entry"),
    url (r'^ckeditor/', include('ckeditor_uploader.urls'))
] 
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]
   