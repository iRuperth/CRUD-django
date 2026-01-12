from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from category.models import Category
from .serializer import BookSerializer

class VistasLibros():
    @api_view(['GET'])
    def BooksList(request):
        libros = Book.objects.all()
        serializer = BookSerializer(libros, many=True)
        return Response(serializer.data)
    
    @api_view(['POST'])
    def BooksCreate(request):
        data = request.data
        categoria_nombres = data.pop('category', [])
        category = Category.objects.filter(category_name__in=category_name)

        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            book = serializer.create({
                **serializer.validated_data,
                'category': category
            })
            response_serializer = BookSerializer(book)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'PUT', 'DELETE'])
    def BooksDetail(request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = BookSerializer(book)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                updated_book = serializer.update(book, serializer.validated_data)
                updated_serializer = BookSerializer(updated_book)
                return Response(updated_serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)