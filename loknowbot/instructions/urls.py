from django.urls import path

from loknowbot.instructions import views

app_name = 'instructions'

urlpatterns = [
    path('<int:pk>/', views.InstructionDetailView.as_view(), name='instruction-set-detail'),
    path('add/', views.InstructionCreateView.as_view(), name='instruction-set-create'),
    path('list/', views.InstructionListView.as_view(), name='instruction-set-list'),
    path('update/<int:pk>/', views.InstructionUpdateView.as_view(), name='instruction-set-update'),
]
