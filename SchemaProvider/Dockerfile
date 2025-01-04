FROM openjdk:16-ea-14-alpine

ARG JAR_FILE
ARG USER_NAME
ARG USER_PASSWORD
ENV JAR_FILE=${JAR_FILE}
ENV USER_NAME=${USER_NAME}
ENV USER_PASSWORD=${USER_PASSWORD}

RUN apk update && apk add bash

RUN adduser -D -h /work -s /bin/bash schemaService \
  && mkdir -p /work/config \
  && mkdir -p /work/log \
  && mkdir -p /work/app \
  && chown -R schemaService:schemaService /work

COPY target/$JAR_FILE /work/$JAR_FILE

COPY target/lib/ /work/lib/

USER schemaService

RUN cd /work

ENV HOME /work

WORKDIR /work

CMD java -jar -Dspring.datasource.username=${USER_NAME} -Dspring.datasource.password=${USER_PASSWORD} ${JAR_FILE}
