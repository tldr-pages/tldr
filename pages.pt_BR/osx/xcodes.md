# xcodes

> Baixe, instale e gerencie várias versões do Xcode.
> Veja também: `xcodes runtimes`.
> Mais informações: <https://github.com/xcodesorg/xcodes>.

- Lista todas as versões do Xcode instaladas:

`xcodes installed`

- Lista todas as versões do Xcode disponíveis:

`xcodes list`

- Seleciona uma versão do Xcode especificando o número da versão ou um caminho:

`xcodes select {{versao-do-xcode|caminho/para/Xcode.app}}`

- Baixa e instala uma versão específica do Xcode:

`xcodes install {{versao-do-xcode}}`

- Baixa, instala e seleciona a versão mais recente do Xcode:

`xcodes install --latest --select`

- Baixa uma versão específica do Xcode para um diretório específico sem instalá-la:

`xcodes download {{versao-do-xcode}} --directory {{caminho/para/diretorio}}`
