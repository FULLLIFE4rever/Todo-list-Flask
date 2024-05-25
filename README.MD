## О приложении

Это простое приложение для создания списка дел. Позволяет просматривать, создавать, изменять и удалять задачи.

## Настройки файла .env

```MYSQL_PASSWORD=mysql
MYSQL_USER=mysql
MYSQL_PORT=3306
DB_HOST=localhost
DB_NAME=mysql
```

## Запуск приложения
Запустите команды
```
pip install -r requirements.txt
flask db upgrade head
flask run
```
