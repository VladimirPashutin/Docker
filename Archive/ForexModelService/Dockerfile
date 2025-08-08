FROM eclipse-temurin:21
RUN mkdir /opt/app
COPY ./target/forex-model-service-1.5.0.jar /opt/app
RUN apt update
RUN apt install unzip -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN apt install python3-consul -y
RUN apt install python3-psycopg2 -y
RUN apt install python3.12-venv -y
RUN python3 -m venv /opt
RUN /opt/bin/pip install argparse
RUN /opt/bin/pip install tensorflow
RUN /opt/bin/pip install tf2onnx

WORKDIR /opt/app

RUN unzip ./forex-model-service-1.5.0.jar

CMD ["java", "-jar", "./forex-model-service-1.5.0.jar"]
