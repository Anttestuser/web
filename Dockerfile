FROM python:3.10.9-slim

WORKDIR /web

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=root:root . .
RUN chmod -R 777 .

EXPOSE 8000

RUN chmod a+x /web/start.sh