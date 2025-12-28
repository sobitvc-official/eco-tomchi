from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def article_list(request):
    # Faqat suvga oid maqolalarni tartib bilan chiqarish
    articles = Article.objects.all().order_by('-published_date')
    categories = Category.objects.all()
    return render(request, 'articles/index.html', {
        'articles': articles, 
        'categories': categories
    })

def article_detail(request, slug):
    # Prefetch article blocks to render block-based content efficiently
    article = get_object_or_404(Article.objects.prefetch_related('blocks'), slug=slug)
    categories = Category.objects.all()
    return render(request, 'articles/detail.html', {
        'article': article, 
        'categories': categories
    })

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category).order_by('-published_date')
    categories = Category.objects.all()
    return render(request, 'articles/index.html', {
        'articles': articles, 
        'categories': categories,
        'current_category': category
    })

def about(request):
    categories = Category.objects.all()
    return render(request, 'articles/about.html', {'categories': categories})