# docker build

> Cria uma imagem a partir de um Dockerfile.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/build/>.

- Cria uma imagem docker usando o Dockerfile no diretório atual:

`docker build .`

- Cria uma imagem docker a partir de um Dockerfile em uma URL específica:

`docker build {{github.com/creack/docker-firefox}}`

- Cria uma imagem docker e cria uma etiqueta para ela:

`docker build --tag {{nome:etiqueta}} .`

- Cria uma imagem docker sem contexto de criação:

`docker build --tag {{nome:etiqueta}} - < {{Dockerfile}}`

- Não usa o cache na criação da imagem:

`docker build --no-cache --tag {{nome:etiqueta}} .`

- Cria uma imagem docker usando um Dockerfile específico:

`docker build --file {{Dockerfile}} .`

- Cria uma imagem docker utilizando variáveis customizadas para a criação de imagens:

`docker build --build-arg {{PROXY_DO_HTTP=http://10.20.30.2:1234}} --build-arg {{PROXY_DO_FTP=http://40.50.60.5:4567}} .`
