# docker

> Gerenciador de containers e imagens Docker.
> Alguns subcomandos como `run` tem sua própia documentação de uso.
> Mais informações: <https://docs.docker.com/reference/cli/docker/>.

- Lista todos os containers Docker (em execução e parados):

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- Inicializa um container com um nome personalizado a partir de uma imagem:

`docker {{[run|container run]}} --name {{nome_container}} {{imagem}}`

- Começa ou para um container existente:

`docker container {{start|stop}} {{nome_container}}`

- Extrai uma imagem a partir de um Docker Registry:

`docker {{[pull|image pull]}} {{imagem}}`

- Mostra a lista de imagens já baixadas:

`docker {{[images|image ls]}}`

- Abre um terminal dentro de um container em execução:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{nome_container}} {{sh}}`

- Remove um container parado:

`docker {{[rm|container rm]}} {{nome_container}}`

- Obtém e acompanha o histórico de um container:

`docker {{[logs|container logs]}} {{[-f|--follow]}} {{nome_container}}`
