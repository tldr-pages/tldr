# carthage

> Ferramenta de gerenciamento de dependências para aplicativos Cocoa.
> Mais informações: <https://github.com/Carthage/Carthage>.

- Baixar a versão mais recente de todas as dependências mencionadas no Cartfile e realizar o build delas:

`carthage update`

- Atualizar as dependências, mas faz apenas build para iOS:

`carthage update --platform ios`

- Atualizar as dependências, mas sem realizar build de nenhuma delas:

`carthage update --no-build`

- Download e rebuild da versão atual das dependências (sem atualizá-las):

`carthage bootstrap`

- Rebuild de uma dependência específica:

`carthage build {{dependência}}`
