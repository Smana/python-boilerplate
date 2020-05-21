FROM python:3.8.3-alpine3.11

WORKDIR /app

COPY . /app
RUN pip install --upgrade pip
RUN pip install -e .

EXPOSE 80

ENV PYTHONUNBUFFERED 1
ENTRYPOINT ["myapp"]
