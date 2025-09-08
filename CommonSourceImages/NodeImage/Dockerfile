FROM node:22.12.0-slim
LABEL authors="VPashutin"

COPY .npmrc /root/.npmrc
COPY id_rsa /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa
RUN apt-get update && apt-get install git openssh-client -y
COPY nexus_cert.pem /usr/local/share/ca-certificates/nexus/nexus.crt
RUN update-ca-certificates
RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan bitbucket.org >> ~/.ssh/known_hosts
