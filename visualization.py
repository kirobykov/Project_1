"""
Модуль для визуализации настроений.
"""

import matplotlib.pyplot as plt

def plot_mood_trends(moods):
    """
    Строит график настроений.

    :param moods: Словарь с настроениями
    """
    dates = list(moods.keys())
    scores = [moods[date] for date in dates]

    # Преобразование настроений в числовые значения для графика
    scores_numeric = [3 if mood == "happy" else 2 if mood == "neutral" else 1 for mood in scores]

    plt.plot(dates, scores_numeric, marker='o')
    plt.title('Тренды настроений')
    plt.xlabel('Дата')
    plt.ylabel('Настроение (1 - Sad, 2 - Neutral, 3 - Happy)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()
