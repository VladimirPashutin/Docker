FROM node:14.17 as build-stage
ARG NPM_TOKEN
ENV NPM_TOKEN=$NPM_TOKEN
COPY .npmrc ./.npmrc
COPY package*.json ./
RUN npm install
COPY .env* ./
COPY ./src ./src
COPY ./public ./public
COPY ./vue.config.js ./
RUN npm run build

FROM nginx as production-stage
RUN mkdir /app
COPY --from=build-stage /dist /app
COPY ./nginx.conf /etc/nginx/nginx.conf