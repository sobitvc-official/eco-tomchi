(function(){
  const btn = document.getElementById('theme-toggle');
  const root = document.documentElement;
  function setTheme(name){
    try{
      if(name==='dark') root.classList.add('theme-dark'); else root.classList.remove('theme-dark');
      localStorage.setItem('site-theme', name);
      updateIcons();
    }catch(e){}
  }
  function toggle(){
    const isDark = root.classList.contains('theme-dark');
    setTheme(isDark ? 'light' : 'dark');
  }
  function updateIcons(){
    if(!btn) return;
    const sun = btn.querySelector('.light-icon');
    const moon = btn.querySelector('.dark-icon');
    const isDark = root.classList.contains('theme-dark');
    if(sun) sun.style.display = isDark ? 'none' : 'inline-block';
    if(moon) moon.style.display = isDark ? 'inline-block' : 'none';
  }
  if(btn){
    btn.addEventListener('click', toggle);
    // init icons
    updateIcons();
  }
})();