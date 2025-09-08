FROM eclipse-temurin:23-jdk
LABEL authors="VPashutin"

COPY id_rsa /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa
COPY settings.xml /root/.m2/settings.xml
COPY nexus_cert.pem /usr/local/share/ca-certificates/nexus/nexus.crt
RUN apt-get update && apt-get install git maven unzip openssh-client -y
RUN ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts
RUN update-ca-certificates
RUN keytool -importcert -trustcacerts -noprompt -file /usr/local/share/ca-certificates/nexus/nexus.crt -alias nexus.pashutin.com -keystore "$JAVA_HOME/lib/security/cacerts" -storepass changeit