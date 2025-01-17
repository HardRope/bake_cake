# Сайт магазина тортов на заказ

Это сайт магазина тортов на заказ. Здесь можно заказать превосходные торты на ваш вкус с доставкой на дом.

Выберите торт на сайте или сконструируйте его сами и укажите место доставки. Мы испечём вкуснейший торт по вашему заказу и привезём его вам.

На сайте есть три независимых интерфейса. Первый — это публичная часть, где можно выбрать или сконструировать торт, и быстро оформить заказ без регистрации и SMS.

Второй интерфейс предназначен для менеджера. Здесь происходит обработка заказов. Менеджер видит поступившие новые заказы и первым делом созванивается с клиентом, чтобы подтвердить заказ. После этого менеджер передаёт заказ на исполнение. Затем торт испекут и доставят еду клиенту.

Третий интерфейс — это админка. Преимущественно им пользуются программисты при разработке сайта. Также сюда заходит менеджер, чтобы обновить меню.

## Как установить

Скачайте код:
```
git clone https://github.com/Irina-Kasatkina/bake_cake
```

Перейдите в каталог проекта:
```
cd bake_cake
```

[Установите Python](https://www.python.org/), если вы этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```
python --version
```
**Важно!** Версия Python должна быть не ниже 3.6.

Возможно, вместо команды `python` здесь и в остальных инструкциях этого README придётся использовать `python3`. Зависит это от операционной системы и от того, установлен ли у вас Python старой второй версии. 

В каталоге проекта создайте виртуальное окружение:
```
python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`


Установите зависимости в виртуальное окружение:
```
pip install -r requirements.txt
```
### Переменные окружения

Создайте файл `.env` в каталоге `bake_cake/` и запишите туда следующие переменные окружения в формате `ПЕРЕМЕННАЯ=значение`:
- `ALLOWED_HOSTS`- разрешённые хосты, см. [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE_ENGINE` - движок базы данных, например: `django.db.backends.sqlite3`.
- `DATABASE_NAME` - имя базы данных, например: `places.sqlite3`.
- `DEBUG` - дебаг-режим (поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки).
- `SECRET_KEY` - секретный ключ проекта.

Пример файла `.env`:
```
#
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=db.sqlite3
DEBUG=True
SECRET_KEY=django-insecure-0if40nf4nf93n4
```

## Как запустить

Создайте файл базы данных SQLite и отмигрируйте её следующей командой:

```
python manage.py migrate
```

Создайте суперюзера:

```
python manage.py createsuperuser
```

Запустите сервер:

```
python manage.py runserver
```

После этого сайт будет доступен по адресу `http://127.0.0.1:8000/` в браузере.

Панель администратора будет доступна по адресу `http://127.0.0.1:8000/admin/` в браузере.

## Цели проекта

Код написан в учебных целях — это командный проект в курсе по веб-разработке на Python в [Devman](https://dvmn.org). 
