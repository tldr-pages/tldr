# podman run

> Executar um comando em um novo contêiner Podman.
> Mais informações: <https://docs.podman.io/en/latest/markdown/podman-run.1.html>.

- Executa um comando em um novo contêiner a partir de uma imagem marcada:

`podman run {{imagem:tag}} {{comando}}`

- Executa um comando em um novo contêiner em segundo plano e exibe o ID:

`podman run --detach {{imagem:tag}} {{comando}}`

- Executa um comando em um contêiner temporário no modo interativo e pseudo-TTY:

`podman run --rm --interactive --tty {{imagem:tag}} {{comando}}`

- Executa um comando em um novo contêiner com variáveis de ambiente passadas:

`podman run --env '{{variável}}={{valor}}' --env {{variável}} {{imagem:tag}} {{comando}}`

- Executa um comando em um novo contêiner com volumes montados por bind:

`podman run --volume {{/caminho/para/caminho_no_host}}:{{/caminho/para/caminho_no_contêiner}} {{imagem:tag}} {{comando}}`

- Executa um comando em um novo contêiner com portas publicadas:

`podman run --publish {{porta_no_host}}:{{porta_no_contêiner}} {{imagem:tag}} {{comando}}`

- Executa um comando em um novo contêiner sobrescrevendo o ponto de entrada (entrypoint) da imagem:

`podman run --entrypoint {{comando}} {{imagem:tag}}`

- Executa um comando em um novo contêiner conectando-o a uma rede:

`podman run --network {{rede}} {{imagem:tag}}`
