FROM docker.pashutin.com/spring-image:latest AS build_stage
ARG JAR_NAME
WORKDIR /build
COPY ./target/lib/* ./lib/
COPY ./target/${JAR_NAME}.jar ./application.jar
RUN jlink --add-modules "$(jdeps --ignore-missing-deps -q -recursive --multi-release 23 --print-module-deps --class-path='lib/*' application.jar)" --strip-debug --no-man-pages --no-header-files --compress=zip-6 --output jdk

FROM gcr.io/distroless/cc:latest
LABEL authors="Vladimir Pashutin"

WORKDIR /opt/workspace

COPY --from=build_stage /build/lib ./lib
COPY --from=build_stage /build/jdk /opt/jdk
COPY --from=build_stage /build/application.jar ./

ENTRYPOINT ["/opt/jdk/bin/java", "-jar", "application.jar"]