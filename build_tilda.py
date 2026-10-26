# -*- coding: utf-8 -*-
"""Собирает T123-блоки для Tilda из страниц макета.

Каждая страница -> tilda/<page>/01_main.html (всё до формы) и 02_footer.html (футер).
Между ними в Tilda ставится стандартный блок формы. CSS вшит в блок и заскоуплен под .st,
ассеты — абсолютные ссылки на GitHub Pages.
"""
import os, re, sys
HERE=os.path.dirname(os.path.abspath(__file__))
BASE=sys.argv[1] if len(sys.argv)>1 else 'https://denusa1987-netizen.github.io/stolica-site/'
OUT=os.path.join(HERE,'tilda'); os.makedirs(OUT,exist_ok=True)

css=open(os.path.join(HERE,'assets','style.css'),encoding='utf-8').read()
js=open(os.path.join(HERE,'assets','main.js'),encoding='utf-8').read()

# --- scope css under .st ---
css=css.replace('@font-face{font-family:"Cormorant Garamond";src:url("fonts/CormorantGaramond-Light.ttf") format("truetype");font-weight:300;font-style:normal;font-display:swap}','')
def scope_block(block):
    # block: "selectors{...}" possibly inside @media; prefix each selector
    def pref(m):
        sels=m.group(1); body=m.group(2)
        out=[]
        for s in sels.split(','):
            s=s.strip()
            if not s: continue
            if s in ('html',): continue
            if s=='body': out.append('.st'); continue
            if s=='*': out.append('.st *'); continue
            if s.startswith('body'): out.append('.st'+s[4:]); continue
            if s.startswith(':root'): out.append('.st'+s[5:]); continue
            out.append('.st '+s)
        return ','.join(out)+'{'+body+'}'
    return re.sub(r'([^{}@]+)\{([^{}]*)\}',pref,block)

parts=re.split(r'(@media[^{]+\{(?:[^{}]*\{[^{}]*\})*\s*\}|@keyframes[^{]+\{(?:[^{}]*\{[^{}]*\})*\s*\})',css)
scoped=[]
for p in parts:
    if p.startswith('@media'):
        head,body=p.split('{',1); body=body.rsplit('}',1)[0]
        scoped.append(head+'{'+scope_block(body)+'}')
    elif p.startswith('@keyframes'):
        scoped.append(p)
    else:
        scoped.append(scope_block(p))
css_s=''.join(scoped)
# .st itself gets body styles; also reset Tilda interference
css_s=('.st{font-family:var(--sans);font-weight:300;font-size:18px;line-height:1.6;color:var(--ink);background:var(--cream);overflow-x:hidden}'
       '.st *{box-sizing:border-box}.st .hdr{z-index:1000}.st .modal{z-index:2000}'+css_s)

def convert(page):
    html=open(os.path.join(HERE,page),encoding='utf-8').read()
    body=html.split('<body>',1)[1].split('<script src="assets/main.js">',1)[0]
    body=re.sub(r'<button class="mock-bar">.*?</button>','',body)
    body=body.replace('src="assets/','src="'+BASE+'assets/').replace('poster="assets/','poster="'+BASE+'assets/').replace('data-video="assets/','data-video="'+BASE+'assets/')
    # internal links -> tilda page addresses (same slugs)
    body=re.sub(r'href="([a-z0-9\-]+)\.html(#[a-z0-9\-]+)?"',lambda m:'href="/'+('' if m.group(1)=='index' else m.group(1))+(m.group(2) or '')+'"',body)
    # split at form section
    i=body.find('<section class="sec dark" id="zayavka">')
    if i<0: i=body.find('<footer>')
    main=body[:i]; rest=body[i:]
    main=re.sub(r'<form class="form[^>]*>.*?</form>','',main,flags=re.S)
    main=re.sub(r'<label class="consent[^>]*>.*?</label>','',main,flags=re.S)
    j=rest.find('<footer>')
    footer=rest[j:]
    modal=re.search(r'<div class="modal">.*?</div>',footer,re.S)
    modal_html=modal.group(0) if modal else ''
    footer=footer.replace(modal_html,'')
    head=('<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;300i&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">'
          '<style>'+css_s+'</style>')
    block1=head+'<div class="st">'+main+modal_html+'</div><script>'+js+'</script>'
    block2='<div class="st">'+footer+'</div>'
    d=os.path.join(OUT,page.replace('.html','')); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,'01_main.html'),'w',encoding='utf-8').write(block1)
    open(os.path.join(d,'02_footer.html'),'w',encoding='utf-8').write(block2)
    print(page,len(block1)//1024,'KB +',len(block2)//1024,'KB')

for page in sorted(p for p in os.listdir(HERE) if p.endswith('.html')):
    convert(page)
open(os.path.join(OUT,'_style_scoped.css'),'w',encoding='utf-8').write(css_s)
HEADLINK='<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;300i&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">'
open(os.path.join(OUT,'_head.html'),'w',encoding='utf-8').write(HEADLINK+'<style>'+css_s+'</style>')
