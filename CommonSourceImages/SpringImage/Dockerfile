FROM eclipse-temurin:23-jdk
LABEL authors="VPashutin"

COPY id_rsa /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa
COPY settings.xml /root/.m2/settings.xml
COPY nexus_cert.pem /etc/cert/nexus_cert.pem
RUN apt-get update && apt-get install git maven unzip openssh-client -y
RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan bitbucket.org >> ~/.ssh/known_hosts
RUN keytool -importcert -trustcacerts -noprompt -file /etc/cert/nexus_cert.pem -alias nexus.pashutin.com -keystore "$JAVA_HOME/lib/security/cacerts"