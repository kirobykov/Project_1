# Mood Tracker

## Автор
Быков Кирилл Витальевич, 471786

## Описание
Mood Tracker - это пакет, который позволяет пользователям отслеживать свое настроение в течение нескольких дней. Пользователи могут вводить свое настроение и получать статистику и визуализацию данных.

## Примеры использования

```python
from mood_tracker.tracker import MoodTracker

tracker = MoodTracker()
tracker.add_mood("2023-10-01", "happy")
tracker.add_mood("2023-10-02", "sad")
tracker.add_mood("2023-10-03", "neutral")

print(tracker.get_mood("2023-10-01"))  # Вывод: happy
print(tracker.get_average_mood())  # Вывод: Статистика настроения
