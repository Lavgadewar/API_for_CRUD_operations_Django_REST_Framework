# from django.shortcuts import render
# from book_api.models import Book
# from rest_framework.response import Response
# from book_api.serilizer import BookSerializers
# from rest_framework.decorators import api_view
# # Create your views here.
# @api_view(['GET'])
# def book_list(request):
#     books = Book.objects.all() 
#     seriallizer = BookSerializers(books, many=True)
#     return Response(seriallizer.data) 

# @api_view(['POST'])
# def book_create(request):
#     serializers = BookSerializers(data=request.data)
#     if serializers.is_valid():
#         serializers.save()
#         return Response(serializers.data)
#     else:
#         return Response(serializers.errors)    

# def book


from rest_framework.views import APIView
from book_api.models import Book
from book_api.serilizer import BookSerializers
from rest_framework.response import Response
from rest_framework import status

class BookList(APIView):
    def get(self,request) :
        books = Book.objects.all() 
        seriallizer = BookSerializers(books, many=True)
        return Response(seriallizer.data) 

class BookCreate(APIView):
    def post(self,request ):
        serializers = BookSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  

class BookDetail(APIView):

    def get_book_by_pk(self,pk):
        try:
           return  Book.objects.get(pk=pk)
        except:
           return Response({
            'error': 'book does not exist'
        }, status=status.HTTP_404_NOT_FOUND) 

    def get(self,request,pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializers(book)
        return Response(serializer.data)           
    
    def put(self,request,pk): 
        book = self.get_book_by_pk(pk)
        serializer = BookSerializers(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk): 
        book = self.get_book_by_pk(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
      
