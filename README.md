**! для удобства можно загрузить mp4 файлы и проверить работу анализа через OpenAPI по ссылке: http://localhost:8000/docs.** 
* **/v1/analyze/** — загрузка и анализ видеофайла
* **/v1/metrics** — метрики Prometheus
* **БД**: таблица videos (результаты анализа)

---
Реализовано на **FastAPI**, **SQLAlchemy (async)**, **alembic**, **PostgreSQL (asyncpg)**, **Alembic**, **OpenCV** и **Docker**.

---
Перед тем, как запустить проект, создайте файл .env в папке app/

---
### Запуск проекта через Docker Compose
```bash

docker compose up --build 
```
---
### Применить миграции
```bash

docker compose exec app alembic upgrade head 
```
