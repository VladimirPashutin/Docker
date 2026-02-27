FROM docker.pashutin.com/python-image:latest AS build_stage
ARG REPOSITORY
ARG BRANCH
WORKDIR /build
ENV PIPENV_VENV_IN_PROJECT=1
RUN git clone ${REPOSITORY} .
RUN git checkout ${BRANCH}
RUN pip3 install pipenv
RUN pipenv install --deploy --system --ignore-pipfile

FROM gcr.io/distroless/cc:latest
LABEL authors="Vladimir Pashutin"
ARG SCRIPT_NAME

COPY --from=build_stage /usr/bin/ /usr/bin/
COPY --from=build_stage /usr/lib/ /usr/lib/
COPY --from=build_stage /usr/local/ /usr/local/
COPY --from=build_stage /build/ /opt/workspace/
COPY --from=build_stage /lib/x86_64-linux-gnu/ /lib/x86_64-linux-gnu/
COPY --from=build_stage /build/${SCRIPT_NAME} /opt/workspace/start.py

ENV PATH="/opt/workspace/.venv/bin:$PATH"

WORKDIR /opt/workspace

CMD ["/usr/local/bin/python", "-u", "start.py"]