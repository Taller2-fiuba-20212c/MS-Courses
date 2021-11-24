FROM python:3.7-alpine

RUN pip install fastapi uvicorn pymongo dnspython pydantic

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

COPY ./app /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["./start.sh"]