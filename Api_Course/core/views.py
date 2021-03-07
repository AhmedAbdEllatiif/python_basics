from django.http import JsonResponse
from django.shortcuts import render
from .serializers import PostSerializers
from .models import Post

# rest_framework
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics


def test_view(request):
    return render(request,'test.html')



class PostListView(generics.ListCreateAPIView):

    serializer_class = PostSerializers
    queryset = Post.objects.all()
    
    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()
    
    


# CreateAPIView handles only post method 
# So we must add get method
class PostCreateView(mixins.ListModelMixin,generics.CreateAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    

# GenericAPIView and mixins 
# serializer_class,queryset declaration
# no need for function body by your self
class PostView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
       
        
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
 
        
        



# serializer with APIView
# You must handle errors by yourself
class TextView(APIView):

    permission_classes = (IsAuthenticated,)
    
    def get(self,request,*args,**kwargs):
        qs = Post.objects.all()
        serializer = PostSerializers(qs,many= True)
        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        print(request.data)
        serializer = PostSerializers(data=request.data)
        print(">>>>>>>>>>>>>>USER",self.request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    

""" 
# Stardrad way to make a json response
def text_view(request):
    data = {
        "name":'Ahmed',
         "age": '27',
    }
    
   return JsonResponse(data)
 """
