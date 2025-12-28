from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    # Fayl yuklash uchun (ixtiyoriy)
    featured_image = models.ImageField(upload_to='articles/', blank=True, null=True)
    # INTERNETDAN LINK QO'YISH UCHUN (ASOSIY):
    image_url = models.URLField(max_length=500, blank=True, null=True)
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='articles')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def first_image_block(self):
        """Return the first image block for previewing in lists (or None)."""
        return self.blocks.filter(block_type='image').first()

    @property
    def first_text_block(self):
        """Return the first text block for preview snippets (or None)."""
        return self.blocks.filter(block_type='text').first()

class ArticleBlock(models.Model):
    """Block-based content for articles. Editors can add text or image blocks and style them."""

    BLOCK_TYPES = (
        ('text', 'Text'),
        ('image', 'Image'),
    )

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='blocks')
    order = models.PositiveIntegerField(default=0)
    block_type = models.CharField(max_length=10, choices=BLOCK_TYPES)

    # Rich text for text blocks
    text = RichTextField(blank=True, null=True)

    # Image for image blocks
    image = models.ImageField(upload_to='articles/blocks/', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    image_alt = models.CharField(max_length=255, blank=True)

    # Simple style fields (optional)
    text_color = models.CharField(max_length=30, blank=True)
    font_family = models.CharField(max_length=100, blank=True)
    font_size = models.CharField(max_length=30, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.block_type} #{self.order} for {self.article.title}"
