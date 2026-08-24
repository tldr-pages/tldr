# xcodes runtimes

> Gerencia runtimes do Simulador Xcode.
> Mais informações: <https://github.com/xcodesorg/xcodes#commands>.

- Lista todos os runtimes do Simulador disponíveis:

`xcodes runtimes --include-betas`

- Baixa um runtime do Simulador:

`xcodes runtimes download {{nome-do-runtime}}`

- Baixa e instala um runtime do Simulador:

`xcodes runtimes install {{nome-do-runtime}}`

- Baixa/instala um runtime do Simulador para a versão iOS/watchOS/tvOS/visionOS especificada (diferencia maiúsculo de minúsculo):

`xcodes runtimes {{download|install}} "{{iOS|watchOS|tvOS|visionOS}} {{versão_runtime}}"`

- Define um local específico para onde o pacote do runtime será baixado primeiro (o padrão é `~/Downloads`):

`xcodes runtimes {{download|install}} {{nome_runtime}} --directory {{caminho/para/diretório}}`

- Não exclui o pacote baixado quando o Simulador é instalado com sucesso:

`xcodes runtimes install {{nome_runtime}} --keep-archive`
