from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages   # 👈 para mostrar alertas
from .models import Category, Post
from .forms import ContactForm        # 👈 importamos el formulario


def home(request):
    """Landing con últimos posts de motos y coches"""
    motos = Post.objects.filter(category__slug="motos").order_by("-created_at")[:6]
    coches = Post.objects.filter(category__slug="coches").order_by("-created_at")[:6]
    return render(request, "posts/home.html", {"motos": motos, "coches": coches})


def category_list(request, slug):
    """Lista de posts de una categoría con paginación"""
    category = get_object_or_404(Category, slug=slug)
    post_list = Post.objects.filter(category=category).order_by("-created_at")

    # Paginación: 6 posts por página
    paginator = Paginator(post_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "posts/category_list.html",
        {"category": category, "page_obj": page_obj}
    )


def post_detail(request, slug):
    """Detalle de un post concreto"""
    post = get_object_or_404(Post, slug=slug)
    return render(request, "posts/post_detail.html", {"post": post})


def about(request):
    return render(request, "posts/about.html")


def contact(request):
    """Formulario de contacto"""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # 👈 guarda en la base de datos
            messages.success(request, "¡Tu mensaje ha sido enviado correctamente!")
            return redirect("posts:contact")
    else:
        form = ContactForm()

    return render(request, "posts/contact.html", {"form": form})


def search(request):
    """Buscador de posts por título o contenido"""
    query = request.GET.get("q")
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by("-created_at")
    return render(request, "posts/search.html", {"query": query, "results": results})
