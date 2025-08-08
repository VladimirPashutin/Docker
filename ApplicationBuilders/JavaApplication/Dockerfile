ARG JAVA_IMAGE
FROM ${JAVA_IMAGE} AS build_stage
ARG JAVA_RELEASE
ARG PROJECT_HOME
ARG REPOSITORY
ARG JAR_NAME
ARG BRANCH
WORKDIR /build
ENV RELEASE=${JAVA_RELEASE}
RUN update-ca-certificates
RUN --mount=type=ssh,id=project git clone ${REPOSITORY} .
RUN git checkout ${BRANCH}
WORKDIR /build/${PROJECT_HOME}
RUN --mount=type=secret,id=settings,target=/root/.m2/settings.xml mvn install
RUN jdeps --ignore-missing-deps -q -recursive --multi-release ${RELEASE} --print-module-deps --class-path target/lib/* target/${JAR_NAME}.jar
RUN jlink --add-modules "$(jdeps --ignore-missing-deps -q -recursive --multi-release ${RELEASE} --print-module-deps \
    --class-path target/lib/* target/${JAR_NAME}.jar)" --strip-debug --no-man-pages --no-header-files --compress=zip-6 --output jdk

#FROM datanese/gcr.io-distroless-java:latest
FROM debian:buster-slim
LABEL authors="Vladimir Pashutin"

WORKDIR /opt/workspace

COPY --from=build_stage /opt/build/lib ./lib
COPY --from=build_stage /opt/build/jdk /opt/jdk
COPY --from=build_stage /opt/build/application.jar ./

CMD ["tail","-f","/dev/null"]
#ENTRYPOINT ["/opt/jdk/bin/java", "-jar", "application.jar"]CMD ["./server/index.mjs"]