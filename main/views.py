from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # AccessMixin

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Post
from .forms import PostForm
from .serializers import PostSerializer, PostDetailSerializers



# def home(request):
#    # if request.user.is_authenticated: или is_anonymous
#    posts = Post.objects.all().order_by('-created_at')
#    return render(request, 'main/home.html', {'posts': posts})

# username, password, email, is_active, first_name, last_name, is_staff, is_superuser, last_login, date_joined, get_username()
# some_user.username = other_username
# var1 = some_user.get_username()
# user.get_fullname()
# user.get_short_name()
# user.check_password(request.password)
# user.set_password('new password')
# user.save()
# user.set_unusable_password()
# user.save()
# user.has_usable_password()
# login(request, request.user)


# authenticate(request, username=<username_from_form>, password=<password_from_form>)

# def post_detail(request, id):
#    try:
#        post = Post.objects.get(id=id)
#    except Post.DoesNotExist:
#       pass
#   return render(request, 'main/post_detail.html', {'post': post})


# def second_view(request):
#   return render(request, 'main/second.html')


# def post_create(request):
#   if request.method == 'POST':
#       form = PostForm(request.POST)
#      if form.is_valid():\
#          cd = form.save(commit=False)
#          cd.author = request.user
#          cd.save()
#         return redirect(home)
#  else:
#      form = PostForm()
#   return render(request, 'main/post_create.html', {'form': form})


class PostList(LoginRequiredMixin ,ListView):
    model = Post
    template_name = 'main/home.html'
    content_object_name: str = 'posts'
    ordering = '-created_at'

    def test_func(self):
        return self.request.user.is_authenticated() and

    def get_login_url(self):
        return '/account/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['admin_user'] = User.objects.get(id=1)
        if 'counter' in self.request.session:
            self.request.session['counter'] += 1
            print(f'============= counter={self.request.session["counter"]}')
        else:
            self.request.session['counter'] = 1
        return context




# def render_to_responce(self, context, **responce_kwargs):
#    responce = super().render_to_responce(context, **responce_kwargs)
#    if 'counter' in self.request.COOKIES:
#        cnt = int(self.request.COOKIES.get('counter')) + 1
#        responce.set_cookie('counter', cnt, max_age=5)
#        print(f'--------------- cnt: {cnt} type: {type(cnt)}')
#    else:
#       responce.set_cookie('counter', 1, max_age=5)
#    return responce

class MyMixin:
    def some_method(self, kdif=None):
        return


#   def get_queryset(self):
#       return Post.objects.all().order_by('-created_at')


class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    # model = Post
    form_class = PostForm
    template_name = 'main/post_create.html'
    success_url = '/blog/'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/'


# @api_view(['GET'])
# def api_posts(request):
#    if request.method == 'GET':
#        posts = Post.objects.all()
#        serializer = PostSerializer(posts, many=True)
#        return Response(serializer.data)

# class APIPosts(APIView):
#    def get(self, request):
#        posts = Post.objects.all()
#        serializer = PostSerializer(posts, many = True)
#        return Response(serializer.data)


#    def post(self, request):
#        serializer = PostSerializer(data=request.data)
#        if serializer.is_valid()
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP__400_BAD_REQUEST)


# class APIPosts(ListCreateAPIView):
#    queryset = Post.objects.all()
#    serializer_class = PostSerializer


# class APIDetailPosts(RetrieveUpdateDestroyAPIView):
#    queryset = Post.objects.all()
#    serializer_class = PostDetailSerializer


class  APIPostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def api_detail_posts(request, pk):
    if request.method == 'GET':
        posts = Post.objects.get(pk=pk)
        serializer = PostDetailSerializer(posts)
        return Response(serializer.data)








