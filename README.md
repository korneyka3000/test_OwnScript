## Буров Корней Владимирович
# ТЗ по вакансии Python разработчик от компании Own Script

### Часть первая - создание схемы БД + SQL запросы находится в папке [db_scheme](db_scheme/DB_SCHEME.md)

---

### Часть вторая - управляемый по сети фонарь.

>Python version == 3.10
>
>Реализация сетевого протокола на aiohttp

---

`Для запуска надо:`

- Склонировать репозиторий
    ```bash
    git clone https://github.com/korneyka3000/test_OwnScript.git
    ```
- Перейти в папку проекта
    ```bash
    cd test_OwnScript
    ```
- Создать виртуальное окружение
    ```bash
    python3 -m venv venv
    ```
- Активировать виртуальное окружение для Linux
    ```bash
    . venv/bin/active
    ```
  Или для windows
    ```bash
    venv\Scripts\activate  
    ```
- Установить зависимости
    ```bash
    pip install -r requirements.txt
    ```
- Запустить проект: по умолчанию подключается к `127.0.0.1:9999`
    ```bash
    python main.py
    ```
- Если надо подключить клиента к определённому Хост/Порт используйте `--host` и `--port` соответственно, например:
  ```bash
  python main.py --host 127.0.0.1 --port 3000
  ```