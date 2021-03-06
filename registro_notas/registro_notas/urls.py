"""registro_notas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from core.views import StudentView, ProfessorView, DisciplineView, GradeDisciplineView, GradeStudentView


router = DefaultRouter()
router.register(r'students', StudentView)
router.register(r'professors', ProfessorView)
router.register(r'disciplines', DisciplineView)
router.register(r'grades', GradeDisciplineView)

# NESTED URLS-----------------------------------------
dicipline_router = routers.NestedSimpleRouter(router, r'disciplines', lookup='discipline')
dicipline_router.register(r'grades', GradeDisciplineView)
student_router = routers.NestedSimpleRouter(router, r'students', lookup='student')
student_router.register(r'grades', GradeStudentView)
#-----------------------------------------------------

schema_view = get_swagger_view(title='Grade Register API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-docs/', schema_view),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token)
    # # urls oauth2
    # path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # urls jwt
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls 
urlpatterns += dicipline_router.urls 
urlpatterns += student_router.urls 
