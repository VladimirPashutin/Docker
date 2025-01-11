ARG JAVA_IMAGE
FROM openjdk:${JAVA_IMAGE} AS build_stage
ARG jarname
ARG JAVA_RELEASE
WORKDIR /opt/build
COPY ./target/lib/* ./lib/
ENV RELEASE=${JAVA_RELEASE}
COPY ./target/${jarname}.jar ./application.jar
RUN jlink --add-modules "$(jdeps --ignore-missing-deps -q -recursive --multi-release ${RELEASE} --print-module-deps \
    --class-path 'lib/*' application.jar)" --strip-debug --no-man-pages --no-header-files --compress=zip-6 --output jdk

FROM debian:buster-slim

WORKDIR /opt/workspace

COPY --from=build_stage /opt/build/jdk /opt/jdk
COPY --from=build_stage /opt/build/lib ./lib
COPY --from=build_stage /opt/build/application.jar ./

#CMD ["tail","-f","/dev/null"]
ENTRYPOINT ["/opt/jdk/bin/java", "-jar", "application.jar"]