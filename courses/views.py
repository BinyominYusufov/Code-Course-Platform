from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminOrReadOnly]

class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminOrReadOnly]

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAdminUser]

class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAdminUser]

class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAdminUser]



from rest_framework import generics, permissions
from .models import CourseModule
from .serializers import ModuleSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

class ModuleListView(generics.ListAPIView):
    queryset = CourseModule.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAdminOrReadOnly]

class ModuleDetailView(generics.RetrieveAPIView):
    queryset = CourseModule.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAdminOrReadOnly]

class ModuleCreateView(generics.CreateAPIView):
    queryset = CourseModule.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAdminUser]

class ModuleUpdateView(generics.UpdateAPIView):
    queryset = CourseModule.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAdminUser]

class ModuleDeleteView(generics.DestroyAPIView):
    queryset = CourseModule.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAdminUser]


from rest_framework import generics, permissions
from .models import Course
from .serializers import CourseSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]

class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]

class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]

class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]

class CourseDeleteView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]
