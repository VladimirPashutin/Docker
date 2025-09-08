FROM python:3.12
LABEL authors="VPashutin"

COPY id_rsa /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa
COPY pip.conf /root/.config/pip/pip.conf
RUN apt-get update && apt-get install git openssh-client -y
RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan bitbucket.org >> ~/.ssh/known_hosts
COPY nexus_cert.pem /usr/local/share/ca-certificates/nexus/nexus.crt
RUN update-ca-certificates
