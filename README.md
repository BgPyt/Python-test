# Запуск проекта 
 <code>docker-compose up -d</code>  - Соберет образы и запустит проект
<h3>Запуск тестов из контейнера</h3>
<code>docker exec -it {container_id} bash  
pytest tests</code>
<h3>Возможные проблемы при мастштабировании</h3>
<strong>Увелчение времени на ответ от сервера</strong>:

1) Перенос на асинхронный движок asyncpg и все остальное
2) Кэширование данных прогноза погоды
3) Правильная индексация таблиц
4) использоание распределительный систем (Kubernetes или Docker swarm)


# Тестовое задание на Python-программиста

В этом репозитории реализовано API приложения для планирования пикников, состоящие из сущностей:

    Город
    Пикник
    Пользователь
    Регистрация пользователя на пикник

# Задание

Тестовое задание подразумевает изменение представленного здесь кода для достижения следующих задач:
<h3> Минимальный уровень</h3>

    Запустить проект и ознакомиться с его документацией на странице http://127.0.0.1:8000/redoc/ или http://127.0.0.1:8000/docs/ и выполнить каждый из запросов
    Изменить код проекта для получения дополнительных возможностей:
        Добавить поиск городов аргументом q в запросе /get-cities/
        Добавить возможность фильтрации пользователей по возрасту(минимальный/максимальный) в запросе users-list
        Поправить ошибку в запросе picnic-add
        Добавить метод регистрации на пикник picnic-register
    Высказать идеи рефакторинга файла external_requests.py
    Описать возможные проблемы при масштабировании проекта

<h3>Продвинутый уровень</h3>

    Привести к нормальному виду:
        Методы обращения к эндпойнтам
        Названия эндпойнтов
        Архитектуру и пути обращения к эндпойнтам
    Расписать все входные/выходные поля в документации (/redoc/ или /docs/), описав их классами
    Оптимизировать работу с базой данных в запросе /all-picnics/
    Сменить базу данных с SQLite на PostgreSQL
    Отрефакторить файл external_requests.py
    Написать тесты

<h3>Дополнительные задания</h3>

    Сделать логирование в файл, который не будет очищаться после перезапуска в докере
    Описать правильную архитектуру для проекта

## Запуск проекта 
 <code>docker-compose up -d</code>  Соберет образы и заупистит проект
