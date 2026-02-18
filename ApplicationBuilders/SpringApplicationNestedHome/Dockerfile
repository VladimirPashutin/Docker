FROM docker.pashutin.com/spring-image:latest AS build_stage
ARG PROJECT_HOME
ARG REPOSITORY
ARG JAR_NAME
ARG BRANCH
WORKDIR /build
RUN git clone ${REPOSITORY} .
RUN git checkout ${BRANCH}
WORKDIR /build/${PROJECT_HOME}
RUN mvn install -f /build/${PROJECT_HOME}/pom.xml
RUN jlink --add-modules "$(jdeps --ignore-missing-deps -q -recursive --multi-release 23 --print-module-deps --class-path='target/lib/*' target/${JAR_NAME}.jar)" --strip-debug --no-man-pages --no-header-files --compress=zip-6 --output jdk

FROM gcr.io/distroless/cc:latest
LABEL authors="Vladimir Pashutin"
ARG PROJECT_HOME
ARG JAR_NAME

WORKDIR /opt/workspace

COPY --from=build_stage /build/${PROJECT_HOME}/jdk /opt/jdk
COPY --from=build_stage /build/${PROJECT_HOME}/target/lib ./lib
COPY --from=build_stage /build/${PROJECT_HOME}/target/${JAR_NAME}.jar ./application.jar

CMD ["/opt/jdk/bin/java", "-jar", "application.jar"]