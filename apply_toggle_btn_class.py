import os, re

lessons_dir = 'lessons'
files = sorted([f for f in os.listdir(lessons_dir) if f.endswith('.html')])

for fname in files:
    path = os.path.join(lessons_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update button class to toggle-btn no-math and remove inline background overrides
    html = re.sub(
        r'<button id="view-toggle-btn"[^>]*>(.*?)</button>',
        r'<button id="view-toggle-btn" class="toggle-btn no-math" onclick="toggleViewMode()">\1</button>',
        html
    )

    # 2. Update toggleViewMode JS function to switch class mode-3d
    html = re.sub(
        r'btn\.style\.background = [^;]+;',
        r'if (is3DMode || is3D) { btn.classList.add("mode-3d"); } else { btn.classList.remove("mode-3d"); }',
        html
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Updated toggle button styling in {fname}')

