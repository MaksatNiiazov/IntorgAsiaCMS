document.addEventListener("DOMContentLoaded", function() {
    document.body.classList.add("loaded");
  });

  window.addEventListener('scroll', function() {
    var anchor = document.getElementById('anchor');
    var scrollPercent = (document.documentElement.scrollTop + document.body.scrollTop) / (document.documentElement.scrollHeight - document.documentElement.clientHeight) * 100;
  
    if (scrollPercent >= 10 && scrollPercent < 95) {
      anchor.style.opacity = '0.8';
      anchor.style.pointerEvents = 'all';
    } else {
      anchor.style.opacity = '0';
      anchor.style.pointerEvents = 'none';
    }
  });

  document.getElementById('anchor').addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  var openBtn = document.getElementById('open-btn');
  var anchor = document.getElementById('anchor');
  var popup = document.getElementById('popup');
  var icons = document.querySelectorAll('.icon');

  openBtn.addEventListener('click', function() {
    if (popup.style.opacity === '1') {
      popup.style.opacity = '0';
      popup.style.pointerEvents  = 'none';
    
    } else {
      popup.style.opacity = '1';
      popup.style.pointerEvents  = 'all';
    }
  });

  anchor.addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  for (var i = 0; i < icons.length; i++) {
    icons[i].addEventListener('click', function() {
      // Действия при клике на иконку
      // Например, переход на соответствующую страницу
    });
  }

  // Получаем элемент с идентификатором "open-btn"
var openBtn = document.getElementById("open-btn");

// Функция для добавления анимации тряски
function shakeElement() {
  openBtn.classList.add("shake");

  // Удаление класса "shake" после окончания анимации
  setTimeout(function() {
    openBtn.classList.remove("shake");
  }, 1000); // Длительность анимации в миллисекундах
}

// Запускаем функцию для тряски каждые 5 секунд
setInterval(shakeElement, 5000);
