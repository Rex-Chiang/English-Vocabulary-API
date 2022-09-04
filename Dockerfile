FROM python:3.9-slim-buster
MAINTAINER m41045@gmail.com
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /django-backend
WORKDIR /django-backend
ADD . /django-backend
RUN pip3 install -r requirements.txt
EXPOSE 8010
ENTRYPOINT ["/bin/bash", "docker-entrypoint.sh"]
CMD ["./runserver.sh"]