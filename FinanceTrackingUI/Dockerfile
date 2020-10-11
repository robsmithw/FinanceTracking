FROM node:12.18-stretch-slim as base

WORKDIR /home/app

COPY package.json package-lock.json ./

RUN npm install

COPY . /home/app

EXPOSE 4200
CMD [ "npm", "start", "--", "--host", "0.0.0.0" ]
