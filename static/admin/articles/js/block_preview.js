document.addEventListener('DOMContentLoaded', function () {
  function setupInline(inline) {
    if (!inline) return;
    // Support both old and new admin inline structures
    const colorInput = inline.querySelector('input[name$="text_color"]');
    const fontSelect = inline.querySelector('select[name$="font_family"]');
    const sizeSelect = inline.querySelector('select[name$="font_size"]');

    let preview = inline.querySelector('.block-preview');
    if (!preview) {
      preview = document.createElement('div');
      preview.className = 'block-preview';
      preview.style.border = '1px dashed #e5e7eb';
      preview.style.padding = '8px';
      preview.style.marginTop = '8px';
      preview.style.borderRadius = '6px';
      preview.style.background = '#fff';
      preview.textContent = 'Block preview';
      // try to append after the last control area
      const insertion = inline.querySelector('.form-row') || inline.querySelector('.inline-related') || inline;
      insertion.appendChild(preview);
    }

    // Add palette & presets UI if not present
    if (!inline.querySelector('.palette-row')) {
      const paletteRow = document.createElement('div');
      paletteRow.className = 'palette-row';
      paletteRow.style.marginTop = '6px';

      // Color palette
      const palette = document.createElement('div');
      palette.className = 'color-palette';
      const colors = ['#111827','#0f172a','#0ea5e9','#0369a1','#1e3a8a','#dc2626','#2563eb','#065f46','#b45309','#92400e'];
      colors.forEach(c => {
        const sw = document.createElement('button');
        sw.type = 'button';
        sw.className = 'color-swatch';
        sw.style.background = c;
        sw.style.border = '0';
        sw.style.width = '20px';
        sw.style.height = '20px';
        sw.style.marginRight = '6px';
        sw.style.borderRadius = '4px';
        sw.addEventListener('click', function () {
          if (colorInput) {
            colorInput.value = c;
            colorInput.dispatchEvent(new Event('input'));
            colorInput.dispatchEvent(new Event('change'));
          }
        });
        palette.appendChild(sw);
      });

      // Font presets
      const presetRow = document.createElement('div');
      presetRow.className = 'font-presets';
      presetRow.style.marginTop = '6px';
      const presets = [
        {label: 'Default', font: '', size: ''},
        {label: 'Lead', font: 'Georgia, serif', size: '20px'},
        {label: 'Body', font: '"Helvetica Neue", Arial, sans-serif', size: '16px'},
        {label: 'Small', font: '"Helvetica Neue", Arial, sans-serif', size: '14px'},
      ];
      presets.forEach(p => {
        const b = document.createElement('button');
        b.type = 'button';
        b.className = 'preset-btn';
        b.textContent = p.label;
        b.style.marginRight = '6px';
        b.addEventListener('click', function () {
          if (fontSelect && p.font !== undefined) {fontSelect.value = p.font; fontSelect.dispatchEvent(new Event('change'));}
          if (sizeSelect && p.size !== undefined) {sizeSelect.value = p.size; sizeSelect.dispatchEvent(new Event('change'));}
          // Ensure preview updates
          preview.style.fontFamily = p.font || '';
          preview.style.fontSize = p.size || '';
        });
        presetRow.appendChild(b);
      });

      paletteRow.appendChild(palette);
      paletteRow.appendChild(presetRow);

      const insertion = inline.querySelector('.form-row') || inline;
      insertion.appendChild(paletteRow);

      // Small label
      const help = document.createElement('div');
      help.className = 'palette-help';
      help.textContent = 'Click a swatch to apply a color, or use presets to set font/size.';
      help.style.fontSize = '12px';
      help.style.color = '#6b7280';
      insertion.appendChild(help);
    }

    // Keep the preview in sync with inputs and textarea
    function updatePreview() {
      if (!preview) return;
      preview.style.color = colorInput ? colorInput.value : '';
      preview.style.fontFamily = fontSelect ? fontSelect.value : '';
      preview.style.fontSize = sizeSelect ? sizeSelect.value : '';
      const textarea = inline.querySelector('textarea[name$="text"]');
      if (textarea && textarea.value.trim()) {
        // sanitize minimal: take plain text roughly
        preview.innerHTML = textarea.value.trim().slice(0, 400);
      } else {
        preview.textContent = 'Block preview';
      }
    }

    if (colorInput) colorInput.addEventListener('input', updatePreview);
    if (fontSelect) fontSelect.addEventListener('change', updatePreview);
    if (sizeSelect) sizeSelect.addEventListener('change', updatePreview);
    const ta = inline.querySelector('textarea[name$="text"]');
    if (ta) ta.addEventListener('input', updatePreview);

    // Initialize preview value
    updatePreview();
  }

  function initAll() {
    // initialize existing inlines
    document.querySelectorAll('.inline-group .form-row, .inline-related').forEach(function (node) {
      setupInline(node);
    });
  }

  // On page load
  initAll();

  // Observe DOM mutations to detect dynamically added inlines
  const container = document.querySelector('.inline-group');
  if (container && window.MutationObserver) {
    const observer = new MutationObserver(function (mutations) {
      for (const m of mutations) {
        for (const n of m.addedNodes) {
          if (n.nodeType === 1) {
            // If a new inline was added, try to initialize it
            if (n.classList.contains('inline-related') || n.querySelector('.inline-related') || n.classList.contains('form-row')) {
              setTimeout(() => setupInline(n), 25);
            }
          }
        }
      }
    });
    observer.observe(container, { childList: true, subtree: true });
  }

  // Also handle the 'add-row' click for compatibility
  document.body.addEventListener('click', function (e) {
    if (e.target && (e.target.matches('.add-row a') || e.target.matches('.add-row'))) {
      setTimeout(initAll, 60);
    }
  });

});