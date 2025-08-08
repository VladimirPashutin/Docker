FROM eclipse-temurin:23-jdk
LABEL authors="VPashutin"
RUN apt-get update
RUN apt-get install git -y
RUN apt-get install maven -y
RUN apt-get install unzip -y
RUN apt-get install openssh-client -y
RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan bitbucket.org >> ~/.ssh/known_hosts
RUN mkdir /opt/app
WORKDIR /opt/app

CMD ["java", "-jar", "./application.jar"]