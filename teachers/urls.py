from django.urls import path, include

app_name = 'teachers'

urlpatterns = [
    path('api/', include('teachers.api.urls')),
]
