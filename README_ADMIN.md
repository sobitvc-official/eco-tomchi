Admin editor guide

Overview
- You can compose articles with multiple blocks (text or image) in the Django admin.
- Each `ArticleBlock` has optional styling fields: `text_color`, `font_family`, and `font_size`.

Usage
1. Go to Admin > Articles and open an article.
2. Use the "Add block" button to append a block. Select type: Image or Text.
3. For text blocks, use the CKEditor to edit rich content.
4. In each inline you'll find:
   - A color palette (click a swatch to apply that color to the block text) ✅
   - Font presets (Lead / Body / Small) to quickly set font family and size ✅
   - A live preview pane that updates as you change the color/font/size ✅

Notes
- The font and size values are stored on the block and applied inline at render time.
- If you want drag-to-sort, use the handle on the inline to reorder blocks (powered by `django-admin-sortable2`).
- To add more preset colors or fonts, edit `static/admin/articles/js/block_preview.js` and adjust `colors` and `presets` arrays.
