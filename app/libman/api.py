from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Author, Book, Publicaition
from .serializers import (AuthorSerializer, BookSerializer,
                          PublicaitionSerializer)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Book.objects.filter(created_by=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=['get'], name='Get Publisher Books')
    def get_publisher_books(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Returns:
            [type]: [description]
        """
        id = request.GET.get("id", "")
        queryset = Book.objects.filter(published_by__id=id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], name='Get Author Books')
    def get_author_books(self, request):
        id = request.GET.get("id", "")
        queryset = Book.objects.filter(author__id=id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Author.objects.filter(created_by=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publicaition.objects.all()
    serializer_class = PublicaitionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Publicaition.objects.filter(created_by=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
