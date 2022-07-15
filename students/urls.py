from django.urls import path, include

app_name = 'students'

urlpatterns = [
    path('api/', include('students.api.urls'))
]
