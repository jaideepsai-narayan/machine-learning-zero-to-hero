import os, re

lessons_dir = 'lessons'
files = sorted([f for f in os.listdir(lessons_dir) if f.endswith('.html')])

for fname in files:
    path = os.path.join(lessons_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    original = html
    # Replace quiz-option on view-toggle-btn with toggle-btn no-math
    html = re.sub(
        r'<button id="view-toggle-btn" class="quiz-option"[^>]*>(.*?)</button>',
        r'<button id="view-toggle-btn" class="toggle-btn no-math" onclick="toggleViewMode()">\1</button>',
        html
    )

    # Also update toggleViewMode JS function if it exists
    html = re.sub(
        r'btn\.style\.background = [^;]+;',
        r'if (is3DMode || is3D) { btn.classList.add("mode-3d"); } else { btn.classList.remove("mode-3d"); }',
        html
    )

    if html != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Updated button styling in {fname}')

