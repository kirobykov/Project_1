# Mood Tracker

## Автор
Быков Кирилл Витальевич, 471786

## Описание
Mood Tracker - это пакет, который позволяет пользователям отслеживать свое настроение в течение нескольких дней. Пользователи могут вводить свое настроение и получать статистику и визуализацию данных.

## Установка
Для установки необходимых зависимостей выполните команду:

```bash
pip install -r requirements.txt

# Инициализация трекера настроений
tracker = MoodTracker()
tracker.add_mood("2023-10-01", "happy")
tracker.add_mood("2023-10-02", "sad")
tracker.add_mood("2023-10-03", "neutral")

# Получение настроения
print(tracker.get_mood("2023-10-01"))  # Вывод: happy

# Получение статистики настроений
stats = MoodStatistics(tracker.moods)
print(stats.get_average_mood())  # Вывод: Среднее настроение

# Визуализация настроений
plot_mood_trends(tracker.moods)
