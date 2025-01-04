FROM openjdk:16-ea-14-alpine

ARG JAR_FILE
ENV JAR_FILE ${JAR_FILE}

RUN apk update && apk add bash

RUN adduser -D -h /work -s /bin/bash services \
  && mkdir -p /work/config \
  && mkdir -p /work/log \
  && mkdir -p /work/app \
  && chown -R services:services /work

COPY target/$JAR_FILE /work/$JAR_FILE
RUN cd /work/app && jar xf /work/$JAR_FILE

USER service

ENV HOME /work

WORKDIR /work

ENV JAVA_OPTS ""

CMD java $JAVA_OPTS -cp /work/app org.springframework.boot.loader.JarLauncher
