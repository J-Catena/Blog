# posts/context_processors.py
from .models import Category, Post

def sidebar_data(request):
    return {
        "sidebar_categories": Category.objects.all().order_by("name"),
        "sidebar_latest_posts": Post.objects.order_by("-created_at")[:5],
    }
