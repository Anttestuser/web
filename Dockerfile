FROM python:3.10.9

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN pip install --upgrade pip

RUN apt update

RUN useradd -rms /bin/bash foxuser && chmod 777 /opt /run

WORKDIR /web

RUN mkdir /web/static && mkdir /web/media && chown -R foxuser:foxuser /web && chmod 755 /web

COPY --chown=foxuser:foxuser . .

RUN pip install -r requirements.txt

USER foxuser

CMD ["gunicorn", "-b", "0.0.0.0:8000", "web.wsgi.application"]
