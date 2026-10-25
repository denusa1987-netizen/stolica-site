# -*- coding: utf-8 -*-
"""Генерирует страницы объектов, «О компании» и «Контакты» из данных ниже."""
import os
HERE=os.path.dirname(os.path.abspath(__file__))

HEAD='''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="hdr">
  <div class="wrap">
    <nav>
      <a href="index.html#obj">Объекты</a>
      <a href="about.html">О компании</a>
      <a href="contacts.html">Контакты</a>
    </nav>
    <a class="logo" href="index.html" aria-label="Группа компаний Столица">
      <span class="logo-serif">Столица</span>
      <span class="rule"></span>
      <span class="sub">Группа компаний</span>
    </a>
    <div class="right">
      <a class="tel-txt" href="tel:+79134444040">+7 913 444-40-40</a>
      <a class="btn btn-ghost btn-sm" href="contacts.html#zayavka">Записаться на показ</a>
      <button class="burger" aria-label="Меню"></button>
    </div>
  </div>
</header>
'''

FOOT='''
<footer>
  <div class="wrap">
    <div class="cols">
      <div>
        <div class="logo" style="align-items:flex-start;text-align:left"><span class="logo-serif">Столица</span><span class="rule"></span><span class="sub">Группа компаний</span></div>
        <p style="margin-top:24px;font-size:14px;color:var(--cream-60)">Застройщики группы: ООО «СЗ «Времена года», ООО «СЗ «Дом на Тельмана». Офис продаж — «Квартирный вопрос».</p>
      </div>
      <div><span class="cap">Адрес</span>г. Абакан, ул. Щетинкина, 24, стр. 1<br>деловой центр «Столица», 6 этаж</div>
      <div><span class="cap">Телефон</span><a class="tel" href="tel:+79134444040">+7 913 444-40-40</a><a href="mailto:asi-19@yandex.ru">asi-19@yandex.ru</a></div>
      <div><span class="cap">Разделы</span><ul><li><a href="vremena-goda.html">ЖК «Времена года»</a></li><li><a href="index.html#obj">Объекты</a></li><li><a href="about.html">О компании</a></li><li><a href="contacts.html">Контакты</a></li></ul></div>
    </div>
    <div class="legal"><p>Информация на сайте не является публичной офертой (ст. 437 ГК РФ). Проектные декларации размещены в ЕИСЖС (наш.дом.рф).</p><span>© 2026 ГК «Столица»</span></div>
  </div>
</footer>
<script src="assets/main.js"></script>
</body>
</html>
'''

FORM='''
<section class="sec dark" id="zayavka">
  <div class="wrap">
    <div class="rv"><span class="micro">Заявка</span><h2 style="margin-top:16px;max-width:14em">{h2}</h2></div>
    <form class="form rv d1">
      <div><label>Имя</label><input type="text" placeholder="Как к вам обращаться"></div>
      <div><label>Телефон</label><input type="tel" placeholder="+7"></div>
      <button class="btn btn-primary" type="submit">Заказать звонок</button>
    </form>
    <label class="consent rv d2"><input type="checkbox" checked> Даю согласие на обработку персональных данных</label>
  </div>
</section>
'''

OBJECTS=[
 dict(slug='trudovaya-84', title='«Дом на Тельмана», Трудовая, 84', city='Абакан', status='Сдан · июнь 2025',
      hero='g_trudovaya.webp', h1='Терраса на кровле и лифт из паркинга',
      lead='Десятиэтажный дом на 88 квартир в 400 метрах от «Времён года». Здесь группа впервые сделала террасу на кровле и подземную парковку, из которой лифт поднимает на любой этаж.',
      text='Широкие возможности планировки: от студий 41 м² до квартир 159 м². Терраса на кровле с зоной отдыха и тренажёрами, где каждый найдёт себе занятие. Подземная парковка с вентиляцией, пожаротушением и круглосуточным видеонаблюдением.',
      nums=[('10','этажей'),('88','квартир'),('41–159','м², площади квартир'),('2025','сдан, июнь')],
      gallery=[('g_trudovaya_krovlya.webp','Пергола на кровле'),('g_trudovaya_vhod.webp','Входная группа'),('g_trudovaya_dvor.webp','Двор с площадкой'),('g_trudovaya.webp','Фасад')]),
 dict(slug='stofato-10b', title='Дом на Стофато, 10Б', city='Абакан', status='Сдан',
      hero='g_stofato.webp', h1='Кирпичный дом с остеклёнными эркерами',
      lead='Десятиэтажный жилой дом на улице Стофато: тёплый кирпич, тёмные витражи эркеров, благоустроенный двор.',
      text='Квартиры с эркерами и панорамным остеклением, закрытый двор с детской площадкой и парковкой для жителей. Дом построен и заселён.',
      nums=[('10','этажей'),('1','подъезд'),('Абакан','ул. Стофато, 10Б'),('Сдан','заселён')],
      gallery=[('g_stofato.webp','Фасад'),('g_stofato_render.webp','Проектный вид')]),
 dict(slug='tregubenko-58', title='Дом на Трегубенко, 58', city='Минусинск', status='Сдан',
      hero='g_tregubenko.webp', h1='Девять этажей кирпича в центре Минусинска',
      lead='Многоквартирный кирпичный дом с магазинами в первом этаже и закрытым двором.',
      text='Квартиры с высокими окнами и тёплыми кирпичными стенами, первый этаж — для магазинов и сервисов, двор — для жителей.',
      nums=[('9','этажей'),('Минусинск','ул. Трегубенко, 58'),('Сдан','заселён'),('1','очередь')],
      gallery=[('g_tregubenko.webp','Фасад'),('g_tregubenko_render.webp','Проектный вид')]),
 dict(slug='delovoy-centr', title='Деловой центр «Столица»', city='Абакан', status='Сдан',
      hero='g_dc.webp', h1='Офисы в центре Абакана',
      lead='Деловой центр на улице Щетинкина, 24: офисы, кафе и собственный офис продаж группы на шестом этаже.',
      text='Здесь работает «Квартирный вопрос» — официальный представитель ГК «Столица». Приходите посмотреть планировки и обсудить условия покупки.',
      nums=[('6','этажей'),('Щетинкина','24, стр. 1'),('9–18','часы работы офиса продаж'),('Абакан','центр города')],
      gallery=[('g_dc.webp','Фасад'),('g_dc2.webp','Вид с улицы')]),
 dict(slug='hudozhestvennaya-shkola', title='Художественная школа им. Д. И. Каратанова', city='Абакан', status='Сдан · социальный объект',
      hero='g_school.webp', h1='Волнистая кровля и арочные витражи',
      lead='Детская художественная школа имени Каратанова — социальный объект группы: светлые мастерские, высокие окна, узнаваемый силуэт.',
      text='Здание построено для города: арочные витражи, двусветные залы и волнистая кровля, которую видно с улицы издалека.',
      nums=[('3','этажа'),('Абакан','центр'),('Сдан','работает'),('Школа','искусств')],
      gallery=[('g_school.webp','Фасад'),]),
]

def obj_page(o):
    nums=''.join(f'<div class="rv"><div class="num">{a}</div><div class="cap">{b}</div></div>' for a,b in o['nums'])
    gal=''.join(f'<figure class="rv"><img src="assets/img/{f}" alt=""><figcaption>{c}</figcaption></figure>' for f,c in o['gallery'])
    body=f'''
<section class="hero" id="top">
  <img class="bg" src="assets/img/{o['hero']}" alt="{o['title']}">
  <div class="wrap">
    <div>
      <span class="micro">{o['city']} · {o['status']}</span>
      <h1>{o['h1']}</h1>
      <div class="actions"><a class="btn btn-primary" href="contacts.html#zayavka">Записаться на показ</a><a class="btn btn-ghost" href="index.html#obj">Все объекты</a></div>
    </div>
    <div class="aside"><b>{o['title']}</b>{o['city']}</div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="lead-block">
      <div class="rv"><span class="micro">Объект</span><h2 style="margin-top:16px">{o['title']}</h2></div>
      <div class="rv d1"><p class="lead">{o['lead']}</p><p style="margin-top:22px">{o['text']}</p></div>
    </div>
    <div class="nums">{nums}</div>
    <div class="grid3">{gal}</div>
  </div>
</section>
'''+FORM.format(h2='Расскажем об объекте и покажем планировки')
    return HEAD.format(title=f"{o['title']} — ГК «Столица»", desc=o['lead'])+body+FOOT

ABOUT=HEAD.format(title='О компании — ГК «Столица»', desc='Группа компаний «Столица» строит жилые дома в Абакане и Минусинске с 2005 года.')+'''
<section class="hero" id="top">
  <img class="bg" src="assets/img/g_trudovaya_krovlya.webp" alt="Терраса на кровле">
  <div class="wrap">
    <div>
      <span class="micro">О компании</span>
      <h1>Строим в Хакасии больше двадцати лет</h1>
    </div>
    <div class="aside"><b>ГК «Столица»</b>Абакан · Минусинск</div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="lead-block">
      <div class="rv"><span class="micro">Кто мы</span><h2 style="margin-top:16px">Своя архитектура, свои дворы, свой офис продаж</h2></div>
      <div class="rv d1">
        <p class="lead">Группа компаний «Столица» — застройщик с собственным видением: кирпичные фасады, террасы на кровле, дворы с площадками и подземные паркинги.</p>
        <p style="margin-top:22px">Официальный представитель группы — офис продаж «Квартирный вопрос», работает с 2005 года. Застройщики группы: ООО «СЗ «Дом на Тельмана» (с 2018 года) и ООО «СЗ «Времена года» (с 2026 года). Расчёты по новым домам — через эскроу-счета.</p>
        <p style="margin-top:16px">Руководитель группы — Малахов Николай Николаевич. Директор застройщика — Макеева Наталья Александровна.</p>
      </div>
    </div>
    <div class="nums">
      <div class="rv"><div class="num">2005</div><div class="cap">год основания офиса продаж</div></div>
      <div class="rv d1"><div class="num">6</div><div class="cap">объектов построено и строится</div></div>
      <div class="rv d2"><div class="num">2</div><div class="cap">города: Абакан и Минусинск</div></div>
      <div class="rv d3"><div class="num">90</div><div class="cap">квартир строится во «Временах года»</div></div>
    </div>
  </div>
</section>
<section class="sec dark">
  <div class="wrap">
    <div class="rv"><span class="micro">Как мы строим</span><h2 style="margin-top:16px;max-width:14em">Каждый новый дом — чуть лучше предыдущего</h2></div>
    <div class="feat">
      <div class="rv"><span class="k">01</span><h3>Кирпич и монолит</h3><p>Тёплые кирпичные фасады на монолитном каркасе: долговечно, тихо, красиво стареет.</p></div>
      <div class="rv d1"><span class="k">02</span><h3>Крыша — для жителей</h3><p>Террасы на кровле появились в «Доме на Тельмана» и стали правилом для новых домов.</p></div>
      <div class="rv d2"><span class="k">03</span><h3>Паркинг под домом</h3><p>Лифт из подземного паркинга на свой этаж — чтобы дорога домой заканчивалась у двери.</p></div>
    </div>
  </div>
</section>
'''+FORM.format(h2='Познакомимся лично в офисе продаж')+FOOT

CONTACTS=HEAD.format(title='Контакты — ГК «Столица»', desc='Офис продаж ГК «Столица»: Абакан, ул. Щетинкина, 24, стр. 1, 6 этаж. +7 913 444-40-40.')+'''
<section class="hero" id="top" style="min-height:520px;height:70vh">
  <img class="bg" src="assets/img/g_dc.webp" alt="Деловой центр «Столица»">
  <div class="wrap">
    <div>
      <span class="micro">Контакты</span>
      <h1>Приходите в офис продаж</h1>
    </div>
    <div class="aside"><b>Деловой центр «Столица»</b>ул. Щетинкина, 24, стр. 1, 6 этаж</div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="lead-block">
      <div class="rv">
        <span class="micro">Офис продаж «Квартирный вопрос»</span>
        <h2 style="margin-top:16px">Абакан, Щетинкина, 24</h2>
        <p style="margin-top:22px">Деловой центр «Столица», строение 1, 6 этаж.<br>С понедельника по пятницу, с 9:00 до 18:00.</p>
        <p style="margin-top:22px"><a href="tel:+79134444040" style="font-family:var(--serif);font-size:44px;line-height:1.1">+7 913 444-40-40</a><br>8 (3902) 215-182 · 8 (3902) 215-108<br><a href="mailto:asi-19@yandex.ru">asi-19@yandex.ru</a></p>
        <a class="btn btn-ghost" style="margin-top:28px;color:var(--forest)" href="https://2gis.ru/abakan/firm/70000001029304060" target="_blank" rel="noopener">Открыть в 2ГИС</a>
      </div>
      <div class="rv d1">
        <iframe title="Карта" src="https://yandex.ru/map-widget/v1/?ll=91.442546%2C53.724443&z=16&pt=91.442546%2C53.724443%2Cpm2dgl" width="100%" height="460" frameborder="0" style="display:block;filter:grayscale(.3) sepia(.15)"></iframe>
      </div>
    </div>
  </div>
</section>
'''+FORM.format(h2='Оставьте телефон — перезвоним в рабочее время')+FOOT

for o in OBJECTS:
    open(os.path.join(HERE,f"{o['slug']}.html"),'w',encoding='utf-8').write(obj_page(o))
open(os.path.join(HERE,'about.html'),'w',encoding='utf-8').write(ABOUT)
open(os.path.join(HERE,'contacts.html'),'w',encoding='utf-8').write(CONTACTS)
print('pages:',[o['slug'] for o in OBJECTS],'about','contacts')
