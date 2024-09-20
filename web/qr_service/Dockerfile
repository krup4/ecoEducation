FROM alpine:latest

WORKDIR /app

RUN apk add nodejs npm

COPY ./qrcode.min.js .
COPY ./db.js .
COPY ./package.json .
COPY ./index.html .
COPY ./index.js .
COPY ./qr_server.js .
COPY ./easy.qrcode.js .

RUN npm i

CMD ["node", "qr_server.js"]

