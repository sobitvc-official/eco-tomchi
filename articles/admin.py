from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from adminsortable2.admin import SortableInlineAdminMixin
from .models import Article, Category, ArticleBlock

FONT_CHOICES = [
    ('', '— Default —'),
    ('"Helvetica Neue", Arial, sans-serif', 'Helvetica / Arial'),
    ('Georgia, serif', 'Georgia'),
    ('"Times New Roman", Times, serif', 'Times New Roman'),
    ('"Courier New", monospace', 'Courier New'),
    ('"Merriweather", serif', 'Merriweather (serif)'),
]

FONT_SIZE_CHOICES = [
    ('', '— Default —'),
    ('13px', '13px'),
    ('14px', '14px'),
    ('16px', '16px'),
    ('18px', '18px'),
    ('20px', '20px'),
    ('22px', '22px'),
]

# Preset styles for admin hints (not stored) - good for JS
STYLE_PRESETS = {
    'lead': {'font': 'Georgia, serif', 'size': '20px'},
    'body': {'font': '"Helvetica Neue", Arial, sans-serif', 'size': '16px'},
    'small': {'font': '"Helvetica Neue", Arial, sans-serif', 'size': '14px'},
}

class ArticleBlockForm(forms.ModelForm):
    class Meta:
        model = ArticleBlock
        fields = '__all__'
        widgets = {
            'text': CKEditorWidget(config_name='default'),
            'text_color': forms.TextInput(attrs={'type': 'color'}),
            'font_family': forms.Select(choices=FONT_CHOICES),
            'font_size': forms.Select(choices=FONT_SIZE_CHOICES),
        }

class ArticleBlockInline(SortableInlineAdminMixin, admin.StackedInline):
    model = ArticleBlock
    extra = 1
    form = ArticleBlockForm
    fields = ('order', 'block_type', 'text', 'image', 'image_url', 'image_alt', 'text_color', 'font_family', 'font_size')
    ordering = ('order',)
    readonly_fields = ()

    class Media:
        js = ('/static/admin/articles/js/block_preview.js',)
        css = {
            'all': ('/static/admin/articles/css/block_preview.css',)
        }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

from adminsortable2.admin import SortableAdminBase

@admin.register(Article)
class ArticleAdmin(SortableAdminBase, admin.ModelAdmin):
    # list_display faqat models.py dagi maydonlar bilan mos bo'lishi shart
    list_display = ('title', 'category', 'published_date') 
    list_filter = ('category', 'published_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ArticleBlockInline]

@admin.register(ArticleBlock)
class ArticleBlockAdmin(admin.ModelAdmin):
    list_display = ('article', 'order', 'block_type')
    list_filter = ('block_type', 'article')
    ordering = ('article', 'order')