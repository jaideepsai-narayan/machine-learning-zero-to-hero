import os, re

lessons_dir = 'lessons'
files = sorted([f for f in os.listdir(lessons_dir) if f.endswith('.html')])

replacements = [
    (r'rac\{', r'\\frac{'),
    (r'rac\{', r'\\frac{'),
    (r'	ext\{', r'\\text{'),
    (r'ext\{', r'\\text{'),
    (r'	heta', r'\\theta'),
    (r'heta', r'\\theta'),
    (r'ight\]', r'\\right]'),
    (r'	o ', r'\\to '),
    (r'zsh\.5', r'0.5'),
    (r'zsh\.15', r'0.15'),
    (r'zsh', r'\\to '),
    (r' lpha', r'\\alpha'),
    (r'Continuous number \( \\in \\mathbb\{R\}\$\)', r'Continuous number ($y \\in \\mathbb{R}$)'),
    (r'Probability \(y=1\) \\in \[0, 1\]\$', r'Probability $P(y=1) \\in [0, 1]$'),
    (r'For  > 2\$ classes', r'For $K > 2$ classes'),
    (r'If true label  = 1\$', r'If true label $y = 1$'),
    (r'If true label  = 0\$', r'If true label $y = 0$'),
    (r'\+\\infty0', r'+\\infty'),
]

for fname in files:
    path = os.path.join(lessons_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content)

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Cleaned corruptions in {fname}')

