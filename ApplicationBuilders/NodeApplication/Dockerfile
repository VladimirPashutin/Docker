FROM docker.pashutin.com/node:latest AS build_stage
ARG REPOSITORY
ARG BRANCH
RUN --mount=type=ssh,id=project git clone ${REPOSITORY} .
RUN git checkout ${BRANCH}
RUN --mount=type=secret,id=npmrc,target=./.npmrc npm install
RUN npm run build

FROM gcr.io/distroless/nodejs22-debian12
LABEL authors="Vladimir Pashutin"
COPY --from=build_stage /opt/app/.output/ /opt/app
WORKDIR /opt/app

CMD ["./server/index.mjs"]