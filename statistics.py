"""
Модуль для статистики настроений.
"""

class MoodStatistics:
    """
    Класс для вычисления статистики настроений.
    """

    MOOD_SCALE = {
        "happy": 3,
        "neutral": 2,
        "sad": 1
    }

    def __init__(self, moods):
        """
        Инициализирует объект статистики настроений.

        :param moods: Словарь с настроениями
        """
        self.moods = moods

    def get_average_mood(self):
        """
        Вычисляет среднее настроение.

        :return: Среднее настроение (float)
        """
        total_score = sum(self.MOOD_SCALE[mood] for mood in self.moods.values() if mood in self.MOOD_SCALE)
        count = len(self.moods)
        return total_score / count if count > 0 else 0
