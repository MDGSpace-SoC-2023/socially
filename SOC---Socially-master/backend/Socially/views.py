from django.shortcuts import render
from urllib.request import Request
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404, JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .serializers import PostSerializer, BlogSerializer, LoginSerializer, RegisterSerializer, UserPostSerializer, UserJokesSerializer, MemeSerializer


from .models import RegisterUser,Sample,Blog,Post, LoginUser, RegisterUser, UserPost, UserJokes, Memes


# Create your views here.
# def display(request):
#     return render(request,"login_or_register.html",{})

# def register_page(request):
#     form = forms.RegisterForm()
    
#     if request.method == "POST":
#         form = forms.RegisterForm(request.POST)
#         if form.is_valid():
#             me = User.objects.get(username='Aaryan')
#             print("Validation complete")
#             username1 = form.cleaned_data['username']
#             password1 =  form.cleaned_data['password']
#             image_url1 = form.cleaned_data['image_url']
#             user_input = RegisterUser(username=username1,password= password1, image_url = image_url1,published_date = timezone.now(),user = me)
#             user_input.save()
#             return render(request,'welcome.html',{})
#     return render(request,'registerpage.html',{'form':form})
    
    

# def login_page(request):
#     form = forms.LoginForm()
    
#     if request.method == "POST":
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             print("Validation complete")
#             username =  form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             all_entries = RegisterUser.objects.all()
#             print(all_entries)
#             q1 = RegisterUser.objects.filter(username__startswith=username)
#             q2 = q1.filter(password__startswith=password)
#             if(q2):
#                 return render(request,'welcome.html',{})
#             else:
#                 return render(request,'failed.html',{})
            
#     return render(request,'loginpage.html',{'form':form})

# def blog_list(request):
#     blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request,"blog_list.html",{'blogs':blogs})
    
# def blog_detail(request, pk):
#     blog = get_object_or_404(Blog, pk=pk)
#     return render(request, 'blog_detail.html', {'blog': blog})
# def blog_edit(request):
#     form = forms.BlogForm()
#     if request.method == "POST":
#         form = forms.BlogForm(request.POST)
#         if form.is_valid():
#             print("Validation complete! ")
#             type = form.cleaned_data['type']
#             title = form.cleaned_data['title']
#             content = form.cleaned_data['content']
#             user_input = Blog(type=type,content = content, title= title, published_date = timezone.now())
#             user_input.save()
#             return redirect('literature')
#         else:
#             form = BlogForm()
#     return render(request,"blog_edit.html",{'form':form})
        
# def post_list(request):
#     return render(request,"post_list.html",{})



class UserPostView(APIView):
    
    def get(self, request, id):
        post = Post.objects.get(id=id)
        data = PostSerializer(post).data
        return Response(data)
    @csrf_exempt
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if(serializer.is_valid()): 
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    @csrf_exempt
    def patch(self, request, id, format=None):
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    @csrf_exempt
    def delete(self, request, id, format=None):
        post = Post.objects.get(id=id)
        post.delete()
        return Response(status=204)
    
class UserPostsView(APIView):
    @csrf_exempt
    def get(self, request, username):
        post = Post.objects.filter(author__username=username)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)






class UserBlogView(APIView):
    
    def get(self, request, id):
        post = Blog.objects.get(id=id)
        data = BlogSerializer(post).data
        return Response(data)
    @csrf_exempt
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = BlogSerializer(data=data)
        if(serializer.is_valid()): 
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    @csrf_exempt
    def patch(self, request, id, format=None):
        post = Blog.objects.get(id=id)
        serializer = BlogSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    @csrf_exempt
    def delete(self, request, id, format=None):
        post = Blog.objects.get(id=id)
        post.delete()
        return Response(status=204)
    
class UserBlogsView(APIView):
    @csrf_exempt
    def get(self, request):
        post = Blog.objects.all()
        serializer = BlogSerializer(post, many=True)
        return Response(serializer.data)


# class LoginUserView(APIView):
#     @csrf_exempt
#     def get(self, request,username,password):
#         post = RegisterUser.objects.all()
#         first = post.filter(username=username)
#         second = post.filter(password=password)
#         if(second)
#         serializer = BlogSerializer(post, many=True)
#         return Response(serializer.data)

# def contact(request):
#     if request.method == 'POST'
#     form = SignUpForm(request.P)


class UserPostView(APIView):
    
    def get(self, request, id):
        post = UserPost.objects.get(id=id)
        data = UserPostSerializer(post).data
        return Response(data)
    @csrf_exempt
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserPostSerializer(data=data)
        if(serializer.is_valid()): 
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    @csrf_exempt
    def patch(self, request, id, format=None):
        post = UserPost.objects.get(id=id)
        serializer = UserPostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    @csrf_exempt
    def delete(self, request, id, format=None):
        post = UserPost.objects.get(id=id)
        post.delete()
        return Response(status=204)
    
class UserPostsView(APIView):
    @csrf_exempt
    def get(self, request):
        post = UserPost.objects.all()
        serializer = UserPostSerializer(post, many=True)
        return Response(serializer.data)





@api_view(['POST'])
def api_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'detail': 'Login successful'})
    else:
        return Response({'detail': 'Invalid credentials'}, status=401)

@api_view(['POST'])
def api_logout(request):
    logout(request)
    return Response({'detail': 'Logout successful'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_user_details(request):
    return Response({
        'username': request.user.username,
        'email': request.user.email,
        'password': request.user.password
        # Add more user details as needed
    })

    
class UserJokeView(APIView):
    
    def get(self, request, id):
        post = UserJokes.objects.get(id=id)
        data = UserJokesSerializer(post).data
        return Response(data)
    @csrf_exempt
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserJokesSerializer(data=data)
        if(serializer.is_valid()): 
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    @csrf_exempt
    def patch(self, request, id, format=None):
        post = UserJokes.objects.get(id=id)
        serializer = UserJokesSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    @csrf_exempt
    def delete(self, request, id, format=None):
        post = UserJokes.objects.get(id=id)
        post.delete()
        return Response(status=204)
    
class UserJokesView(APIView):
    @csrf_exempt
    def get(self, request):
        post = UserJokes.objects.all()
        serializer = UserJokesSerializer(post, many=True)
        return Response(serializer.data)
    


class UserMemeView(APIView):
    
    def get(self, request, id):
        post = Memes.objects.get(id=id)
        data = MemeSerializer(post).data
        return Response(data)
    @csrf_exempt
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = MemeSerializer(data=data)
        if(serializer.is_valid()): 
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    @csrf_exempt
    def patch(self, request, id, format=None):
        post = Memes.objects.get(id=id)
        serializer = MemeSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    @csrf_exempt
    def delete(self, request, id, format=None):
        post = Memes.objects.get(id=id)
        post.delete()
        return Response(status=204)
    
class UserMemesView(APIView):
    @csrf_exempt
    def get(self, request):
        post = Memes.objects.all()
        serializer = MemeSerializer(post, many=True)
        return Response(serializer.data)
    

class RegisterView(APIView):
    
    def get(self, request, id):
        post = Memes.objects.get(id=id)
        data = MemeSerializer(post).data
        return Response(data)
    @csrf_exempt
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = MemeSerializer(data=data)
        if(serializer.is_valid()): 
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    @csrf_exempt
    def patch(self, request, id, format=None):
        post = Memes.objects.get(id=id)
        serializer = MemeSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    @csrf_exempt
    def delete(self, request, id, format=None):
        post = Memes.objects.get(id=id)
        post.delete()
        return Response(status=204)
    
class UserMemesView(APIView):
    @csrf_exempt
    def get(self, request):
        post = Memes.objects.all()
        serializer = MemeSerializer(post, many=True)
        return Response(serializer.data)