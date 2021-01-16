# docker build

> Cria uma imagem a partir de um Dockerfile.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/build/>.

- Cria uma imagem docker usando o Dockerfile presente no diretório atual:

`docker build .`

- Cria uma imagem docker usando o Dockerfile de uma URL específica:

`docker build {{github.com/creack/docker-firefox}}`

- Cria uma imagem docker e cria uma tag para ela:

`docker build --tag {{nome:tag}} .`

- Não usa o cache na criação da imagem:

`docker build --no-cache --tag {{nome:tag}} .`

- Cria uma imagem docker usando um Dockerfile específico:

`docker build --file {{Dockerfile}} .`

- Cria uma imagem docker utilizando variáveis customizadas para a criação de imagens:

`docker build --build-arg {{PROXY_DO_HTTP=http://10.20.30.2:1234}} --build-arg {{PROXY_DO_FTP=http://40.50.60.5:4567}} .`
