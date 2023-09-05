### Описание проекта:

Данный проект является API для основного проекта "Poster"

### Как запустить проект:

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
### Примеры запросов к API:

Пример на получение всех постов (GET):

```
http://127.0.0.1:8000/api/v1/posts/
```

Пример на получение конкретного поста (GET):

В качестве параметра <post_id> необходимо передать id интересующего поста, если поста с указанным id не будет найдено, ответ вернется с ошибкой 404

```
http://127.0.0.1:8000/api/v1/posts/<post_id>/
```

В качестве ответа будет получено один или несколько экземпляров модели Post в формате JSON:

```
{
    "id": <int>,
    "author": <str>,
    "image": <null or str>,
    "text": <str>,
    "pub_date": <date>,
    "group": <null or int>
}
```
