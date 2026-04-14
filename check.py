import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all script blocks
scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
print(f"Found {len(scripts)} script blocks\n")

for i, script in enumerate(scripts):
    # Remove comments for analysis
    cleaned = re.sub(r'//.*$', '', script, flags=re.MULTILINE)
    cleaned = re.sub(r'/\*.*?\*/', '', cleaned, flags=re.DOTALL)
    
    # Count braces
    opens = cleaned.count('{')
    closes = cleaned.count('}')
    parens_open = cleaned.count('(')
    parens_close = cleaned.count(')')
    
    print(f"Script block {i+1}: {len(script)} chars")
    print(f"  Braces: {{ {opens} }} {closes} -> {'BALANCED' if opens == closes else 'MISMATCH!'}")
    print(f"  Parens: ( {parens_open} ) {parens_close} -> {'BALANCED' if parens_open == parens_close else 'MISMATCH!'}")
    
    # Look for function definitions
    funcs = re.findall(r'function\s+(\w+)\s*\(', cleaned)
    print(f"  Functions defined: {funcs[:15]}{'...' if len(funcs)>15 else ''}")
    
    # Check for common errors
    if 'const' in cleaned:
        const_count = cleaned.count('const')
        print(f"  const declarations: {const_count}")
        
    print()

# Check HTML structure
print("\n=== HTML Structure ===")
body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
if body_match:
    body_content = body_match.group(1)
    print(f"Body length: {len(body_content)} chars")
    
    # Check for key elements
    elements = ['id="page-overview"', 'id="page-dynamic"', 'stat-card', 'nav-link', 'detailModal']
    for elem in elements:
        count = body_content.count(elem)
        print(f"  '{elem}': {count}")
