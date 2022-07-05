from django.urls import path, include

app_name = 'courses'

urlpatterns = [
    path('api/', include('courses.api.urls'))
]