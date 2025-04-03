document.addEventListener('DOMContentLoaded', function () {
    // Получаем все элементы с классом achievement-item
    const modalTriggers = document.querySelectorAll('.achievement-item');
    // Получаем все модальные окна
    const modals = document.querySelectorAll('.modal');
    // Получаем все кнопки закрытия модальных окон
    const closeButtons = document.querySelectorAll('.close');

    // Функция для открытия модального окна
    function openModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.style.display = 'block';
        }
    }

    // Функция для закрытия модального окна
    function closeModal(modal) {
        modal.style.display = 'none';
    }

    // Добавляем обработчики событий для каждого достижения
    modalTriggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
            const targetModalId = trigger.getAttribute('data-modal'); // Получаем ID модального окна
            openModal(targetModalId); // Открываем соответствующее модальное окно
        });
    });

    // Добавляем обработчики событий для кнопок закрытия
    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const modal = button.closest('.modal'); // Находим ближайшее модальное окно
            closeModal(modal); // Закрываем его
        });
    });

    // Закрытие модального окна при клике вне его содержимого
    modals.forEach(modal => {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                closeModal(modal);
            }
        });
    });
});