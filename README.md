# SE-test-task

<hr>

Стек:
<ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://www.docker.com/get-started/">Docker</a></li>
    <li><a href="https://fastapi-tutorial.readthedocs.io/en/latest/">FastAPI</a></li>
    <li><a href="https://docs.python.org/3/library/socket.html">Sockets</a></li>
    <li><a href="https://www.mongodb.com/">MongoDB</a></li>
    <li><a href="https://docs.celeryq.dev/en/stable/getting-started/introduction.html">Celery</a> + <a href="https://redis.io/">Redis</a></li>
</ul>

<hr>

<h3>Инструкция по установке</h3>

1) Склонировать репозиторий командой `git clone https://github.com/ArseniyZh/SE-test-task`.
2) Открыть репозиторий в консоли и перейти в папку `app`.
3) Настроить `.env`-файлы (значения по умолчанию уже стоят).
4) Выполнить `docker-compose up -d --build`

<em>
Примечание по установке: <br>
- Перед установкой убедиться, что у вас установлен <a href="https://www.python.org/">Python</a>, 
<a href="https://www.docker.com/get-started/">Docker</a>, <a href="https://git-scm.com/">Git</a> 
и все работает корректно. <br>
- После выполнения `docker-compose up -d --build` требуется немного подождать, пока все сервисы
заработают и синхронизируются.
</em>

<br>

<h3>Documentation</h3>

<h4>Endpoint: `/api/receive_data`</h4>
METHOD: POST <br>
BODY: {payload: int, datetime: datetime}

<h4>Endpoint: `/api/control_signals`</h4>
METHOD: GET <br>
PARAMS: start_time; end_time <br>
Параметры должны быть строкой формата <em>"%Y-%m-%dT%H:%M:%S"</em>
 
