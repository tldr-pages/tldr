# choco source

> Gerenciar fontes para pacotes com Chocolatey.
> Mais informações: <https://chocolatey.org/docs/commands-source>.

- Lista fontes atualmente disponíveis:

`choco source list`

- Adiciona uma nova fonte de pacotes:

`choco source add --name {{nome}} --source {{url_da_fonte}}`

- Adiciona uma nova fonte de pacotes com credenciais:

`choco source add --name {{nome}} --source {{url_da_fonte}} --user {{nome}} --password {{senha}}`

- Adiciona uma nova fonte de pacotes com certificado do cliente:

`choco source add --name {{nome}} --source {{url_da_fonte}} --cert {{caminho/para/certificado}}`

- Habilita uma fonte de pacotes:

`choco source enable --name {{nome}}`

- Desabilita uma fonte de pacotes:

`choco source disable --name {{nome}}`

- Remove uma fonte de pacotes:

`choco source remove --name {{nome}}`
