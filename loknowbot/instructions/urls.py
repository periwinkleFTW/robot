from django.urls import path

from loknowbot.instructions import views

urlpatterns = [
    path('<int:slug>/', views.InstructionSetDetailView.as_view(), name='instruction-set-detail'),
    path('add/', views.InstructionCreateView.as_view(), name='instruction-create'),
    path('list/', views.InstructionSetListView.as_view(), name='instruction-list'),
]
