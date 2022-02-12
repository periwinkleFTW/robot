from django.urls import path

from loknowbot.instructions import views

app_name = 'instructions'

urlpatterns = [
    path('<int:slug>/', views.InstructionDetailView.as_view(), name='instruction-set-detail'),
    path('add/', views.InstructionCreateView.as_view(), name='instruction-set-create'),
    path('list/', views.InstructionListView.as_view(), name='instruction-set-list'),
]
