from django.test import TestCase
from django.urls import reverse
from .models import Article, Category, ArticleBlock

class ArticleBlockModelTest(TestCase):
    def setUp(self):
        self.cat = Category.objects.create(name='News')
        self.article = Article.objects.create(title='Test Article', slug='test-article', content='Base content', category=self.cat)

    def test_block_order_and_str(self):
        b1 = ArticleBlock.objects.create(article=self.article, order=1, block_type='text', text='First')
        b2 = ArticleBlock.objects.create(article=self.article, order=2, block_type='text', text='Second')
        blocks = list(self.article.blocks.all())
        self.assertEqual(blocks[0], b1)
        self.assertEqual(blocks[1], b2)
        self.assertIn('First', str(b1))

class ArticleDetailViewTest(TestCase):
    def setUp(self):
        self.cat = Category.objects.create(name='News')
        self.article = Article.objects.create(title='View Article', slug='view-article', content='Default content', category=self.cat)
        ArticleBlock.objects.create(article=self.article, order=1, block_type='text', text='Block content')

    def test_detail_view_renders_blocks(self):
        url = reverse('articles:article_detail', kwargs={'slug': self.article.slug})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Block content')

class AdminFormWidgetTest(TestCase):
    def test_articleblock_form_widgets(self):
        from .admin import ArticleBlockForm
        form = ArticleBlockForm()
        # CKEditorWidget is used for the text field
        from ckeditor.widgets import CKEditorWidget
        self.assertIsInstance(form.fields['text'].widget, CKEditorWidget)
        # text_color should be an input with type=color
        widget = form.fields['text_color'].widget
        self.assertTrue(hasattr(widget, 'attrs'))
        self.assertEqual(widget.attrs.get('type'), 'color')
