from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Router
#from .permissions import IsOwnerOrReadOnly, IsAuthenticated
from .serializers import RouterSerializer
from .pagination import CustomPagination

class get_delete_update_movie(RetrieveUpdateDestroyAPIView):
    serializer_class = RouterSerializer
    #permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            router = Router.objects.get(pk=pk)
        except Router.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return router

    # Get a movie
    def get(self, request, pk):

        router = self.get_queryset(pk)
        serializer = RouterSerializer(router)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a movie
    def put(self, request, pk):
        
        router = self.get_queryset(pk)

        if(request.user == router.creator): # If creator is who makes request
            serializer = RouterSerializer(router, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a movie
    def delete(self, request, pk):

        router = self.get_queryset(pk)

        if(request.user == router.creator): # If creator is who makes request
            router.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class get_post_movies(ListCreateAPIView):
    serializer_class = RouterSerializer
    #permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       routers = Router.objects.all()
       return routers

    # Get all movies
    def get(self, request):
        routers = self.get_queryset()
        paginate_queryset = self.paginate_queryset(routers)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new movie
    def post(self, request):
        serializer = RouterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

