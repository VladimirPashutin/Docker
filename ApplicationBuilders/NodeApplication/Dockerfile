FROM docker.pashutin.com/node-image:latest AS build_stage
ARG REPOSITORY
ARG BRANCH
WORKDIR /opt/app
RUN git clone ${REPOSITORY} .
RUN git checkout ${BRANCH}
RUN npm install
RUN npm run build

FROM gcr.io/distroless/nodejs22-debian12
LABEL authors="Vladimir Pashutin"
COPY --from=build_stage /opt/app/.output/ /opt/app
WORKDIR /opt/app

CMD ["./server/index.mjs"]