ARG NODE_VERSION=22.12.0
ARG DISTROLESS_VERSION=gcr.io/distroless/nodejs22-debian12
FROM node:${NODE_VERSION}-slim AS build_stage
COPY ./package.json /app/
ARG SERVER_PORT=3000
WORKDIR /app
COPY ./assets ./assets
COPY ./components ./components
COPY ./composables ./composables
COPY ./layouts ./layouts
COPY ./middleware ./middleware
COPY ./pages ./pages
COPY ./plugins ./plugins
COPY ./public ./public
COPY ./server ./server
COPY ./utils ./utils
COPY ./.env ./
COPY ./.npmrc ./
COPY ./app.vue ./
COPY ./auth.d.ts ./
COPY ./error.vue ./
COPY ./nuxt.config.ts ./
COPY ./tsconfig.json ./
RUN npm config set strict-ssl false
RUN npm install
RUN npm run build

#FROM ${DISTROLESS_VERSION}
#LABEL authors="Vladimir Pashutin"
#COPY --from=build_stage /app/.output/ /opt/app
#WORKDIR /opt/app

ENV PORT=${SERVER_PORT}
ENV HOST=0.0.0.0
EXPOSE ${SERVER_PORT}
CMD ["node", ".output/server/index.mjs"]