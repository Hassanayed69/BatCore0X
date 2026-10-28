import os
p = r'C:\Users\bg\OneDrive\Documents\Default Project\batcore\src\styles\main.css'
with open(p, encoding='utf-8', errors='ignore') as f:
    s = f.read()
# print around background
for i,l in enumerate(s.splitlines()):
    if 'background' in l.lower() or l.strip().startswith('html') or l.strip().startswith('body') or l.strip().startswith(':root'):
        print(i+1, repr(l))
        # print next 2
        for j in range(i+1, min(i+4, len(s.splitlines()))):
            print('  ', repr(s.splitlines()[j]))
        print('--')
        if i>200: break
