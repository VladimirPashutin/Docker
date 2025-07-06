FROM eclipse-temurin:23-jdk
LABEL authors="VPashutin"
ARG jarname
ARG JAVA_RELEASE
RUN apt-get update
RUN apt-get install unzip -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN mkdir /opt/app
WORKDIR /opt/app
COPY ./target/lib/* ./lib/
ENV RELEASE=${JAVA_RELEASE}
COPY ./target/${jarname}.jar ./application.jar
RUN unzip ./application.jar
RUN pip install --break-system-packages --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r ./requirements.txt

CMD ["java", "-jar", "./application.jar"]