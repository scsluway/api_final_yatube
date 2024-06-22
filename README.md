# api_final


## Описание:

Проект ***API_FINAL_YATUBE*** - это **API**, основаный на протоколе **REST**, предоставляющий возможности для создания социальной сети. С помощью YATUBE API пользователи могут создавать посты, комментировать их и подписываться друг на друга, обмениваясь информацией и взаимодействуя с интересным контентом.

## Информация о проекте:

 Стек технологий: Python 3.9.13, Django, Django REST Framework, Simple JWT;

 Спецификация API: Доступна в файле `api_final_yatube\yatube_api\static\redoc.yaml`;

 Автор проекта: [scsluway](https://github.com/scluway).

## Инструкция к установке:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:yandex-praktikum/api_final_yatube.git
```

Перейти в корень проекта API_Final_Yatube:

```
cd api_final_yatube/
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

Активировать виртуальное окружение:

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Перейти в рабочую директорию проекта, в которой лежит файл *manage.py*:

```
cd yatube_api/
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Ресурсы API:

### JWT-токен:

    /api/v1/jwt/create/: 
     
  **POST**: Получение JWT-токена.
  
    /api/v1/jwt/refresh/: 
  
  **POST**: Обновление JWT-токена.
         
    /api/v1/jwt/verify/

  **POST**: Проверка JWT-токена.
         
### Посты:

     /api/v1/posts/:
     
  **GET**: Получение списка постов.
  
  **POST**: Создание нового поста.
  
     /api/v1/posts/{post_id}:
     
  **GET**: Получение информации о конкретном посте.
  
  **PUT**: Обновление данных поста.
  
  **PATCH**: Частичное обновление данных поста.
  
  **DELETE**: Удаление поста.

### Группы:

     /api/v1/groups/:
     
  **GET**: Получение списка групп.
  
     /api/v1/groups/{id}:
     
  **GET**: Получение информации о конкретной группе.
         
### Комментарии:
 
     /api/v1/posts/{post_id}/comments/:
  **GET**: Получение списка комментариев к посту.
  
  **POST**: Добавление нового комментария к посту.
  
    /api/v1/posts/{post_id}/comments/{comment_id}:
     
  **GET**: Получение информации о конкретном комментарии.
  
  **PUT**: Обновление данных комментария.
  
  **PATCH**: Частичное обновление данных комментария.
  
  **DELETE**: Удаление комментария.
         
### Подписки:
 
     /api/v1/follow/:
     
  **GET**: Получение списка подписок пользователя.
  
  **POST**: Подписка на другого пользователя.
