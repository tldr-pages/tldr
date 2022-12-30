# finger

> Programa de pesquisa de informações do usuário.
> Mais informações: <https://manned.org/finger>.

- Exibe informações sobre usuários conectados no momento:

`finger`

- Exibe informações sobre um usuário específico:

`finger {{nome_de_usuário}}`

- Exibe o nome de login do usuário, nome real, nome do terminal e outras informações:

`finger -s`

- Produz o formato de saída de várias linhas exibindo as mesmas informações que `-s`, bem como o diretório pessoal do usuário, número de telefone residencial, shell de login, status de correio, etc.:

`finger -l`

- Impede a correspondência com os nomes de usuário e usa apenas nomes de login:

`finger -m`
