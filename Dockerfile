FROM python:3.10.9

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN pip install --upgrade pip

RUN apt update

RUN adduser -rms /bin/bash web_user && chmod 777 /opt /run

WORKDIR /web

RUN mkdir /web/static && mkdir /web/media && chown -R web_user:web_user /web && chmod 755 /web

COPY --chown=web_user:web_user . .

RUN pip install -r requirements.txt

USER web_user

RUN chmod a+x /web/

CMD ["gunicorn", "-b", "0.0.0.0:8000", "web.wsgi.application"]
