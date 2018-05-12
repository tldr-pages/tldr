FROM node:8.11.1-alpine
RUN apk update
RUN apk add python make g++
RUN npm install --unsafe-perm -g tldr
RUN apk del python make g++
ENTRYPOINT ["tldr"]
CMD ["--help"]
