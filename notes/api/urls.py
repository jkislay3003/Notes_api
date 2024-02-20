
from django.urls import path
from .views import UserCreateView, NoteCreateView, NoteDetailView, NoteShareView, NoteUpdateView, NoteVersionHistoryView,UserLoginView

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('notes/create/', NoteCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('notes/share/<int:pk>/', NoteShareView.as_view(), name='note-share'),
    path('notes/update/<int:pk>/', NoteUpdateView.as_view(), name='note-update'),
    path('notes/version-history/<int:pk>/', NoteVersionHistoryView.as_view(), name='note-version-history'),
]
