(function(){
  // header
  var hdr=document.querySelector('.hdr');
  function onScroll(){hdr.classList.toggle('solid',window.scrollY>60);}
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();

  // mobile menu
  var burger=document.querySelector('.burger');
  if(burger){var nav=document.querySelector('.hdr nav');var m=document.createElement('div');m.className='mnav';m.innerHTML=nav?nav.innerHTML:'';(hdr.parentElement||document.body).appendChild(m);burger.addEventListener('click',function(){m.classList.toggle('on');hdr.classList.add('solid');});m.addEventListener('click',function(){m.classList.remove('on');});}

  // reveal
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12});
  document.querySelectorAll('.rv').forEach(function(el){io.observe(el);});

  // divider parallax (transform only)
  var divs=[].slice.call(document.querySelectorAll('.divider img,.divider video'));
  function par(){divs.forEach(function(m){var r=m.parentElement.getBoundingClientRect();var p=(r.top+r.height/2-innerHeight/2)/innerHeight;m.style.transform='scale(1.08) translateY('+(p*-40)+'px)';});}
  if(!matchMedia('(prefers-reduced-motion: reduce)').matches&&location.search.indexOf('static')<0){window.addEventListener('scroll',par,{passive:true});par();}

  // accordion
  document.querySelectorAll('.acc').forEach(function(acc){
    var pic=document.querySelector(acc.dataset.pic);
    var items=acc.querySelectorAll('.acc-item');
    function open(it){
      items.forEach(function(i){i.classList.toggle('open',i===it);});
      if(pic){var imgs=pic.querySelectorAll('img');imgs.forEach(function(im){im.classList.toggle('on',im.dataset.key===it.dataset.key);});}
    }
    items.forEach(function(it){it.querySelector('button').addEventListener('click',function(){open(it);});});
    open(items[0]);
  });

  // carousel nav
  document.querySelectorAll('.car-nav').forEach(function(nav){
    var car=document.querySelector(nav.dataset.for);
    nav.querySelector('.prev').addEventListener('click',function(){car.scrollBy({left:-460,behavior:'smooth'});});
    nav.querySelector('.next').addEventListener('click',function(){car.scrollBy({left:460,behavior:'smooth'});});
  });

  // video modal
  var modal=document.querySelector('.modal');
  if(modal){
    var v=modal.querySelector('video');
    document.querySelectorAll('[data-video]').forEach(function(b){b.addEventListener('click',function(){v.src=b.dataset.video;modal.classList.add('on');v.play();});});
    function close(){modal.classList.remove('on');v.pause();v.removeAttribute('src');v.load();}
    modal.querySelector('.x').addEventListener('click',close);
    modal.addEventListener('click',function(e){if(e.target===modal)close();});
    document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
  }

  // mock bar
  var mb=document.querySelector('.mock-bar');
  if(mb){mb.addEventListener('click',function(){document.body.classList.toggle('show-unc');mb.textContent=document.body.classList.contains('show-unc')?'Скрыть непроверенное':'Показать непроверенное';});}

  // forms (mock)
  document.querySelectorAll('form').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();alert('Макет: заявка отправится после сборки в Tilda.');});});
})();
