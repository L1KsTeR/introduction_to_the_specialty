# 1. Базовый лёгкий образ Python
FROM python:3.13-slim

# 2. Рабочая директория внутри контейнера
WORKDIR /app

# 3. Копируем только файл зависимостей (слой кэшируется, если requirements не менялись)
COPY requirements.txt .

# 4. Устанавливаем зависимости без кэша pip (уменьшает размер образа)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копируем остальной код приложения
COPY . .

# 6. Создаём непривилегированного пользователя (best practice для безопасности)
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# 7. Открываем порт
EXPOSE 5000

# 8. Запуск приложения (debug выключен для.prod-подобного запуска)
CMD ["python", "app.py"]
