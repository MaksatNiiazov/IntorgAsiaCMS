document.querySelectorAll(".wrapper").forEach((wrapper) => {
    const carousel = wrapper.querySelector(".carousel");
    const cards = [...carousel.children];
    const arrowLeft = wrapper.querySelector(".arrow.left");
    const arrowRight = wrapper.querySelector(".arrow.right");
    const firstCardWidth = carousel.querySelector(".card").offsetWidth;

    let isDragging = true,
        isAutoPlay = true,
        startX = 0,
        startScrollLeft = 0,
        timeoutId;

    // Количество видимых карточек
    const cardsPerView = Math.round(carousel.offsetWidth / firstCardWidth);

    // Дублирование карточек для бесконечной прокрутки
    cards.slice(-cardsPerView).reverse().forEach(card => {
        carousel.insertAdjacentHTML("afterbegin", card.outerHTML);
    });
    cards.slice(0, cardsPerView).forEach(card => {
        carousel.insertAdjacentHTML("beforeend", card.outerHTML);
    });

    // Устанавливаем начальную позицию прокрутки
    carousel.classList.add("no-transition");
    carousel.scrollLeft = carousel.offsetWidth;
    carousel.classList.remove("no-transition");

    // Привязываем стрелки к действиям
    arrowLeft.addEventListener("click", () => {
        carousel.scrollLeft -= firstCardWidth;
    });

    arrowRight.addEventListener("click", () => {
        carousel.scrollLeft += firstCardWidth;
    });

    // Обработка начала перетаскивания
    const dragStart = (e) => {
        isDragging = true;
        carousel.classList.add("dragging");
        startX = e.pageX || e.touches[0].pageX;
        startScrollLeft = carousel.scrollLeft;
    };

    // Обработка перетаскивания
    const dragging = (e) => {
        if (!isDragging) return;
        const x = e.pageX || e.touches[0].pageX;
        const distance = x - startX;
        carousel.scrollLeft = startScrollLeft - distance;
    };

    // Завершение перетаскивания
    const dragStop = () => {
        isDragging = false;
        carousel.classList.remove("dragging");
    };

    // Бесконечная прокрутка
    const infiniteScroll = () => {
        if (carousel.scrollLeft === 0) {
            carousel.classList.add("no-transition");
            carousel.scrollLeft = carousel.scrollWidth - (2 * carousel.offsetWidth);
            carousel.classList.remove("no-transition");
        } else if (Math.ceil(carousel.scrollLeft) === carousel.scrollWidth - carousel.offsetWidth) {
            carousel.classList.add("no-transition");
            carousel.scrollLeft = carousel.offsetWidth;
            carousel.classList.remove("no-transition");
        }

        // Сбрасываем автопрокрутку при взаимодействии
        clearTimeout(timeoutId);
        if (!wrapper.matches(":hover")) autoPlay();
    };

    // Автопрокрутка
    const autoPlay = () => {
        if (window.innerWidth < 800 || !isAutoPlay) return;
        timeoutId = setTimeout(() => {
            carousel.scrollLeft += firstCardWidth;
        }, 2500);
    };

    // Слушатели событий для перетаскивания
    carousel.addEventListener("mousedown", dragStart);
    carousel.addEventListener("mousemove", dragging);
    document.addEventListener("mouseup", dragStop);

    carousel.addEventListener("touchstart", dragStart);
    carousel.addEventListener("touchmove", dragging);
    carousel.addEventListener("touchend", dragStop);

    // Слушатели для бесконечной прокрутки
    carousel.addEventListener("scroll", infiniteScroll);
    wrapper.addEventListener("mouseenter", () => clearTimeout(timeoutId));
    wrapper.addEventListener("mouseleave", autoPlay);

    // Запуск автопрокрутки
    // autoPlay();
});
