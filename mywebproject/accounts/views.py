from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Article
from .forms import ArticleForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def home(request):
    """
    Renders the home page.

    Args:
        request: HTTP request

    Returns:
        Rendered home page
    """
    return render(request, 'accounts/home.html')

def signup_view(request):
    """
    Handles user registration.

    If the request is a GET, renders the signup page.
    If the request is a POST, processes the submitted form and creates a new user.

    Args:
        request: HTTP request

    Returns:
        If request is a GET, rendered signup page.
        If request is a POST and the form is valid, redirects to the login page.
        If request is a POST and the form is invalid, rendered signup page with form errors.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
        # Check if username and email are unique
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken.')
            return redirect('register')
        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'You have been registered. Please login to continue.')
        return redirect('login')
    else:
        return render(request, 'accounts/signup.html')

def login_view(request):
    """
    Handles user login.

    If the request is a GET, renders the login page.
    If the request is a POST, processes the submitted form and logs the user in.

    Args:
        request: HTTP request

    Returns:
        If request is a GET, rendered login page with authentication form.
        If request is a POST and form is valid, redirects to the home page.
        If request is a POST and form is invalid, rendered login page with form errors.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # log the user in
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def create_article(request):
    """
    Handles creating a new article.

    If the request is a GET, renders the article form.
    If the request is a POST, processes the submitted form and creates a new article.

    Args:
        request: HTTP request

    Returns:
        If request is a GET, rendered article form.
        If request is a POST and form is valid, redirects to the articles page.
        If request is a POST and form is invalid, rendered article form with form errors.
    """
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, 'Your article has been created!')
            return redirect('articles')
    else:
        form = ArticleForm()
    return render(request, 'accounts/create_article.html', {'form': form})

def articles(request):
    """
    Renders the articles page with all the articles sorted by date.

    Args:
        request: HTTP request

    Returns:
        Rendered articles page with all the articles sorted by date.
    """
    articles = Article.objects.all().order_by('-date_posted')
    return render(request, 'accounts/articles.html', {'articles': articles})

def article_detail(request, pk):
    """
    Renders the page displaying details of a particular article.

    Args:
        request: HTTP request
        pk: The primary key of the article to display details for.

    Returns:
        Rendered page displaying details of the article.
    """
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'accounts/article_detail.html', {'article': article})

def logout_view(request):
    """
    Logs out the currently authenticated user and redirects to the home page.

    Args:
        request: HTTP request

    Returns:
        Redirect to home page after logging out the user.
    """
    logout(request)
    return redirect('home')

