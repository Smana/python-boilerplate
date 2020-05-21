FROM python:3.8.3-alpine3.11

WORKDIR /app

COPY . /app
RUN pip install --upgrade pip
RUN pip install -e .


RUN adduser -h /app -s /bin/false -DH smana \
    && chown -R smana. /app

USER smana

ENV PYTHONUNBUFFERED 1
ENTRYPOINT ["myapp"]
