# ДЗ-2 DOCKER

## Локально без docker-compose 
### Запускаем clickhouse
Создадим тома где будет лежать наша ДБ
```command
docker volume create CH_DB
```

Создаем внутреннюю сеть докера для наших контейнеров
```command
docker network create ch_network
```

Запустим клик
```command
docker run --rm -d --name ch -p 8123:8123 --network ch_network -v CH_DB:/var/lib/clickhouse clickhouse/clickhouse-server
```

- `--rm` после остановки контейнера удалить контейнер
- `--d` запустить в фоновом режиме, не блокирую терминал
- `--name ch` дать имя ch запускаемому контейнеру  
- `-p 8123:8123` пробросить порт хост:контейнер
- `--network ch_network` указываем внутреннюю сеть докера, через которую будет конект из другого контейнера
- `-v CH_DB:/var/lib/clickhouse` прокидываем тома
 
### Запускаем тестовое приложение (симулятор работы сервиса с бд)
Для начала его нужно собрать
```command
docker build -t my_app .
```

Запускаем симулятор работы сервиса с бд
```command
docker run --rm -d --name my_app -m 256m  --network ch_network -v ./my_python_app:/usr/src/app/my_python_app -e CH_HOST=ch -e CH_USER=default -e CH_PASSWORD="" -e CH_PORT=9000  my_app
```

- `-m 256m` ограничиваем память контейнеру в 256 мб
- `-e CH_HOST=ch` Указываем переменные окружения для подключения к клику через внутреннюю сеть докера
- `-e CH_USER=default`
- `-e CH_PASSWORD=""`
- `-e CH_PORT=9000`

## docker-compose
```command
docker-compouse up -d
```
