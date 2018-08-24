from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import permissions, mixins
from .models import Student, Professor, Discipline, Grade
from .permissions import IsProfessor, IsGradeOwner, IsNotAllowed
from .serializers import StudentSerializers, ProfessorSerializers, DisciplineSerializers, GradeSerializers

# Create your views here.

class StudentView(ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializers
	filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
	filter_fields = ('name',)
	search_fields =	('^username',)
	ordering_fields = ('name',)

	def get_permissions(self):    
		if self.request.method in permissions.SAFE_METHODS:	
			return [permissions.AllowAny(),]
		return [permissions.IsAdminUser(),]


class ProfessorView(ModelViewSet):
	queryset = Professor.objects.all()
	serializer_class = ProfessorSerializers
	filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
	filter_fields = ('name',)
	search_fields =	('^username',)
	ordering_fields = ('name',)

	def get_permissions(self):    
		if self.request.method in permissions.SAFE_METHODS:	
			return [permissions.AllowAny(),]
		return [permissions.IsAdminUser(),]


class DisciplineView(ModelViewSet):
	queryset = Discipline.objects.all()
	serializer_class = DisciplineSerializers

	def get_permissions(self):    
		if self.request.method in permissions.SAFE_METHODS:	
			return [permissions.AllowAny(),]
		return [permissions.IsAdminUser(),]


class GradeDisciplineView(ModelViewSet):
	queryset = Grade.objects.all()
	serializer_class = GradeSerializers

	def get_queryset(self):
		try:
			return Grade.objects.filter(discipline= self.kwargs['discipline_pk'])
		except KeyError:
			return Grade.objects.all()

	def get_permissions(self):
		try:
			if not self.request.user.pk == Discipline.objects.get(pk=self.kwargs['discipline_pk']).professor.pk:
				if self.request.method in permissions.SAFE_METHODS:		
					return [IsProfessor(),]		
				else:
					return [IsNotAllowed(),]
			else:
				return [IsProfessor(),]		
		except:
			return [IsProfessor(),]	


class GradeStudentView(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
	queryset = Grade.objects.all()
	serializer_class = GradeSerializers

	def get_queryset(self):
		try:
			return Grade.objects.filter(student= self.kwargs['student_pk'])
		except KeyError:
			return Grade.objects.all()

	def get_permissions(self):		
		try:				
			if not str(self.request.user.pk) == self.kwargs['student_pk']:
				return [IsNotAllowed(),]				
			return []
		except:
			return []
		


