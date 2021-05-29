FROM python:3.9 as builder
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y
RUN apt-get -y install postgresql
RUN apt-get -y  install musl-dev
RUN apt-get -y  install python3-dev
RUN apt-get -y install gcc
RUN pip install --upgrade pip
RUN pip install flake8
COPY . .
#RUN flake8 --ignore=E501,F401 .

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


# pull official base image
FROM python:3.9
RUN mkdir -p /home/app

# create the app user
#RUN addgroup -S app && adduser -S app -G app
RUN adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y

RUN apt-get -y install libpq-dev
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*
COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME
RUN chown -R app:app $APP_HOME

# change to the app user
USER app



# run entrypoint.prod.sh
#ENTRYPOINT ["/home/app/web/entrypoint.sh"]