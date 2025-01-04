FROM openjdk:16-ea-14-alpine

ARG JAR_FILE
ARG USER_NAME
ARG USER_PASSWORD
ENV JAR_FILE ${JAR_FILE}
ENV USER_NAME ${USER_NAME}
ENV USER_PASSWORD ${USER_PASSWORD}

RUN apk update && apk add bash && apk add mc

RUN adduser -D -h /work -s /bin/bash xmlDbXPath \
  && mkdir -p /work/config \
  && mkdir -p /work/log \
  && mkdir -p /work/app \
  && chown -R xmlDbXPath:xmlDbXPath /work

COPY target/$JAR_FILE /work/$JAR_FILE

COPY target/lib/ /work/lib/

USER xmlDbXPath

RUN cd /work

ENV HOME /work

WORKDIR /work

CMD java -jar -Dspring.datasource.username=${USER_NAME} -Dspring.datasource.password=${USER_PASSWORD} ${JAR_FILE}
