from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *
from rest_framework.views import APIView
# Create your views here.



class KinolarViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Kino.objects.all()
    serializer_class = KinoSerializer

    @action(methods=['GET', 'POST'], detail=True)
    def comments(self,request, pk):
        coments = Comment.objects.filter(kino__id=pk)
        serializer = CommentSerializer(coments, many=True)
        return Response({"Success": serializer.data})






# class KinolarAPIView(APIView):
#     def get(self,request):
#         kinolar = Kino.objects.all()
#         serializer = KinoSerializer(kinolar, many=True)
#         return Response({"Barcha kinolar ro'yhati": serializer.data}, status=status.HTTP_200_OK)
#
#     def post(self,request):
#         kino = request.data
#         serializer = KinoSerializer(data=kino)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"Success":serializer.data}, status=status.HTTP_201_CREATED)
#         return Response({"Error": serializer.errors}, status=status.HTTP_501_NOT_IMPLEMENTED)






class AktyorlarViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Aktyor.objects.all()
    serializer_class = AktyorSerializer

# class AktyorlarAPIView(APIView):
#     def get(self,request):
#         aktyorlar = Aktyor.objects.all()
#         serializer = AktyorSerializer(aktyorlar, many=True)
#         return Response({"Success": serializer.data}, status=status.HTTP_200_OK)
#
#     def post(self,request):
#         aktyor = request.data
#         serializer = AktyorSerializer(data=aktyor)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"Success":serializer.data}, status=status.HTTP_201_CREATED)
#         return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# class AktyorAPIView(APIView):
#     def get(self,request, pk):
#         aktyor = Aktyor.objects.get(id=pk)
#         serializer = AktyorSerializer(aktyor)
#         return Response({"Success": serializer.data}, status=status.HTTP_200_OK)
#
#     def put(self, request,pk):
#         aktyor = Aktyor.objects.get(id=pk)
#         serializer = AktyorSerializer(aktyor, data=request.data)
#
#     def delete(self, request, pk):
#         aktyor = Aktyor.objects.get(id=pk)
#         serializer = AktyorSerializer(aktyor)
#         aktyor.delete()
#         return Response({"Success": serializer.data})










class CommentlarAPIView(APIView):
    def get(self,request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response({"Comments List": serializer.data})

    def post(self,request):
        comment = request.data
        serializer = CommentSerializer(data=comment)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"Successfuly created": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"Errors":"Something is wrong!!!!"}, status=status.HTTP_400_BAD_REQUEST)


# class CommentlarViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticated,]
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#     @action(methods=['POST', 'GET'], detail=True)
#     def add(self,request):
#         if request.method == 'POST':
#             comment = request.data
#             serializer = CommentSerializer(data=comment)
#
#             if serializer.is_valid():
#                 serializer.save(user=request.user)
#                 return Response({"Success": serializer.data})
#             return Response({"Errors": serializer.errors})