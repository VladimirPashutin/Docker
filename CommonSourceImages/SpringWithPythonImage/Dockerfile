FROM eclipse-temurin:23-jdk
LABEL authors="VPashutin"
RUN apt-get update
RUN apt-get install git -y
RUN apt-get install maven -y
RUN apt-get install unzip -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install openssh-client -y
RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan bitbucket.org >> ~/.ssh/known_hosts
COPY ./nexus_cert.pem ./
RUN keytool -importcert -trustcacerts -noprompt -file nexus_cert.pem -alias nexus.pashutin.com -keystore "$JAVA_HOME/lib/security/cacerts"
RUN mkdir /opt/app
WORKDIR /opt/app

CMD ["java", "-jar", "./application.jar"]