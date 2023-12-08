from django.urls import path
from .views import SignupView
from .views import login_view, ProfileAPIView, TAApplicationListView, TAApplicationDetailView, CourseListCreateAPIView, CourseRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', login_view, name='login'),
    path('profile/', ProfileAPIView.as_view(), name='profile-api'),
    path('applications/', TAApplicationListView.as_view(), name='ta-application-list'),
    path('applications/<int:pk>/', TAApplicationDetailView.as_view(), name='ta-application-detail'),
    path('courses/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view(), name='course-retrieve-update-destroy'),
]
