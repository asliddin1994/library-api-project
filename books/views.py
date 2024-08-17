from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Books
from .serializers import BooksSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

# Create your views here.

# class BookListApiView(generics.ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer

class BookListApiView(APIView):

    def get(self, request):
        books = Books.objects.all()
        serializer_data = BooksSerializer(books, many=True).data
        data = {
            "status": f"Returned {len(books)} books",
            "books": serializer_data
        }
        return Response(data)


class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class BookDetailApiView(APIView):

    def get(self, request, pk):
        try:
            book = Books.objects.get(id=pk)
            serializer_data = BooksSerializer(book).data

            data = {
                "status": "Succesfull",
                "book": serializer_data
            }
            return Response(data, status=200)
        except Exception:
            data = {
                "status": "Book not found",
                "message": "Book not found"
            }
            return Response(data, status=404)


# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer

class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            book = Books.objects.get_object_or_404(id=pk)
            book.delete()
            return Response({
                "status": True,
                "message": "Kitob uchirildi"
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                "status": False,
                "message": "Kitob topilmadi aqljon"
            }, status=status.HTTP_400_BAD_REQUEST)

# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer

class BookUpdateApiView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Books.objects.all(), id=pk)
        data = request.data
        serializer = BooksSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({
            "status": True,
            "message": f"Book{book_saved} updated successfully",
        })

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer

class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BooksSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                "status": f"books are saved to the database",
                "books": data
            }
            return Response(data)
class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer




class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BookViewset(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    book = Books.objects.all()
    serializer = BooksSerializer(book, many=True)
    return Response(serializer.data)