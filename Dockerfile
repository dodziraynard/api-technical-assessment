# pull official base image
FROM python:3.9.6-alpine

# create directory for the app user
RUN mkdir -p /home/app_user

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create the app user
RUN addgroup -S app_user && adduser -S app_user -G app_user

# create the appropriate directories
ENV HOME=/home/app_user
ENV APP_HOME=$HOME/app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

RUN pip install --upgrade pip

COPY ./solution/requirements.txt $APP_HOME
RUN pip --default-timeout=1000 install -r requirements.txt

# Delet temp build dir.
# RUN apk del build-deps

COPY ./entrypoint.sh $APP_HOME
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.sh
RUN chmod +x  $APP_HOME/entrypoint.sh

# chown all the files to the app user
RUN chown -R app_user:app_user $APP_HOME

# copy project
COPY ./solution $APP_HOME

# run entrypoint.sh
ENTRYPOINT ["/home/app_user/app/entrypoint.sh"]
