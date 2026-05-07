from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .form import SignupForm, loginForm
from django.contrib.auth.decorators import login_required


def landing_view(request):
    return render(request,'landing.html',)

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            User.objects.create_user(
                username=name,
                email=email,
                password=password
            )
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):

    if request.method == 'POST':

        loginf = loginForm(request.POST)

        if loginf.is_valid():

            name = loginf.cleaned_data['name']
            password = loginf.cleaned_data['password']

            user = authenticate(
                request,
                username=name,
                password=password
            )

            if user is not None:

                login(request, user)

                return redirect('dashboard')

            else:

                return render(
                    request,
                    'login.html',
                    {
                        'loginf': loginf,
                        'error': 'Invalid credentials'
                    }
                )

    else:

        loginf = loginForm()

    return render(
        request,
        'login.html',
        {'loginf': loginf}
    )
@login_required
def dashboard_view(request):
    return render(request,'dashboard.html')


# def home(request):
#     return HttpResponse("Welcome to Blog")

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'post_list.html', {'posts': posts})

# def post_detail(request, id):
#     post = Post.objects.get(id=id)
#     return render(request, 'post_detail.html', {'post': post})

# def go_home(request):
#     return redirect('post_list')

# def form(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form=ContactForm()
#     else:
#         form = ContactForm()

#     return render(request, "base.html", {'form': form})



# from django.views.generic import CreateView, DeleteView, ListView,DetailView, UpdateView
# from .models import Post

# class PostListView(ListView):
#     model = Post
#     template_name = 'post_list.html'
    
    
    
# class PostDetailView(DetailView):
#     model = Post
    

# class PostCreateView(CreateView):
#     model = Post
#     fields = ['title', 'content']
#     success_url = reverse_lazy('post_list')
    
# class PostUpdateView(UpdateView):
#     model = Post
#     fields = ['title', 'content']
#     success_url = reverse_lazy('post_list')
    
    
# class PostDeleteView(DeleteView):
#     model = Post
#     success_url = reverse_lazy('post_list')
    
    
# from django.contrib.auth.mixins import LoginRequiredMixin

# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'content']
#     success_url = reverse_lazy('post_list')





# from django.shortcuts import render, get_object_or_404, redirect
# from django.views import View
# from .models import Post
# from .forms import PostForm  # you should create a ModelForm

# # -------------------------
# # LIST VIEW
# # -------------------------
# class PostListView(View):
#     def get(self, request):
#         posts = Post.objects.all()
#         return render(request, 'post_list.html', {'posts': posts})


# # -------------------------
# # DETAIL VIEW
# # -------------------------
# class PostDetailView(View):
#     def get(self, request, pk):
#         post = get_object_or_404(Post, pk=pk)
#         return render(request, 'post_detail.html', {'post': post})


# # -------------------------
# # CREATE VIEW
# # -------------------------
# class PostCreateView(View):
#     def get(self, request):
#         form = PostForm()
#         return render(request, 'post_form.html', {'form': form})

#     def post(self, request):
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#         return render(request, 'post_form.html', {'form': form})


# # -------------------------
# # UPDATE VIEW
# # -------------------------
# class PostUpdateView(View):
#     def get(self, request, pk):
#         post = get_object_or_404(Post, pk=pk)
#         form = PostForm(instance=post)
#         return render(request, 'post_form.html', {'form': form})

#     def post(self, request, pk):
#         post = get_object_or_404(Post, pk=pk)
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#         return render(request, 'post_form.html', {'form': form})


# # -------------------------
# # DELETE VIEW
# # -------------------------
# class PostDeleteView(View):
#     def get(self, request, pk):
#         post = get_object_or_404(Post, pk=pk)
#         return render(request, 'post_confirm_delete.html', {'post': post})

#     def post(self, request, pk):
#         post = get_object_or_404(Post, pk=pk)
#         post.delete()
#         return redirect('post_list')