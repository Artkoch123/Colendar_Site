document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.slider-image');
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    let currentIndex = 0;

    function showImage(index) {
        images.forEach((img, i) => {
            img.classList.toggle('active', i === index);
        });
    }

    prevButton.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        showImage(currentIndex);
    });

    nextButton.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % images.length;
        showImage(currentIndex);
    });

    // Инициализация первого изображения
    showImage(currentIndex);
});

// Функция отображения списка участников

function toggleParticipantsList() {
    const participantsList = document.getElementById('participants-list');
    const arrowIcon = document.getElementById('arrow-icon');

    // Переключаем класс для скрытия/показа списка
    participantsList.classList.toggle('hidden');

    // Поворачиваем стрелочку
    arrowIcon.classList.toggle('rotated');
}