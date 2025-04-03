document.addEventListener('DOMContentLoaded', () => {
    const eventsContainer = document.getElementById('events-container');
    const dateFilter = document.getElementById('date-filter');
    const categoryFilter = document.getElementById('category-filter');

    // Получаем все карточки мероприятий
    const eventCards = Array.from(eventsContainer.querySelectorAll('.event-card'));

    // Функция для сортировки и фильтрации
    function filterAndSortEvents() {
        const selectedDateOrder = dateFilter.value;
        const selectedCategory = categoryFilter.value;

        // Фильтруем по категории
        const filteredEvents = eventCards.filter(card => {
            return selectedCategory === 'all' || card.dataset.category === selectedCategory;
        });

        // Сортируем по дате
        filteredEvents.sort((a, b) => {
            const dateA = new Date(a.dataset.date);
            const dateB = new Date(b.dataset.date);

            if (selectedDateOrder === 'ascending') {
                return dateA - dateB; // По возрастанию
            } else {
                return dateB - dateA; // По убыванию
            }
        });

        // Очищаем контейнер и добавляем отфильтрованные карточки
        eventsContainer.innerHTML = '';
        filteredEvents.forEach(card => eventsContainer.appendChild(card));
    }

    // Добавляем обработчики событий
    dateFilter.addEventListener('change', filterAndSortEvents);
    categoryFilter.addEventListener('change', filterAndSortEvents);
});