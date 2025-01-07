ARG NODE_VERSION=22.12.0
ARG DISTROLESS_VERSION=gcr.io/distroless/nodejs22-debian12
FROM node:${NODE_VERSION}-slim AS build_stage
COPY ./package.json /app/
ARG SERVER_PORT=3000
WORKDIR /app
RUN npm install
COPY ./dist/ /app/

FROM ${DISTROLESS_VERSION}
LABEL authors="Vladimir Pashutin"
COPY --from=build_stage /app /opt/app
WORKDIR /opt/app

EXPOSE ${SERVER_PORT}
CMD ["app.js"]