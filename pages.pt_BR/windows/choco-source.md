# choco source

> Gerenciar fontes para pacotes com Chocolatey.
> Mais informações: <https://docs.chocolatey.org/en-us/choco/commands/source/>.

- Lista fontes atualmente disponíveis:

`choco source list`

- Adiciona uma nova fonte de pacotes:

`choco source add {{[-n|--name]}} {{nome}} {{[-s|--source]}} {{url_da_fonte}}`

- Adiciona uma nova fonte de pacotes com credenciais:

`choco source add {{[-n|--name]}} {{nome}} {{[-s|--source]}} {{url_da_fonte}} {{[-u|--user]}} {{nome}} {{[-p|--password]}} {{senha}}`

- Adiciona uma nova fonte de pacotes com certificado do cliente:

`choco source add {{[-n|--name]}} {{nome}} {{[-s|--source]}} {{url_da_fonte}} --cert {{caminho/para/certificado}}`

- Habilita uma fonte de pacotes:

`choco source enable {{[-n|--name]}} {{nome}}`

- Desabilita uma fonte de pacotes:

`choco source disable {{[-n|--name]}} {{nome}}`

- Remove uma fonte de pacotes:

`choco source remove {{[-n|--name]}} {{nome}}`
