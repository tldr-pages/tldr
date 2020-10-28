# choco source

> Gerenciar fontes para pacotes com Chocolatey.
> Mais informações: <https://chocolatey.org/docs/commands-source>.

- Listar fontes atualmente disponíveis:

`choco source list`

- Adicionar uma nova fonte de pacotes:

`choco source add --name {{nome}} --source {{url_da_fonte}}`

- Adicionar uma nova fonte de pacotes com credenciais:

`choco source add --name {{nome}} --source {{url_da_fonte}} --user {{nome}} --password {{senha}}`

- Adicionar uma nova fonte de pacotes com certificado do cliente:

`choco source add --name {{nome}} --source {{url_da_fonte}} --cert {{caminho/para/o/certificado}}`

- Habilitar uma fonte de pacotes:

`choco source enable --name {{nome}}`

- Desabilitar uma fonte de pacotes:

`choco source disable --name {{nome}}`

- Remover uma fonte de pacotes:

`choco source remove --name {{nome}}`
