# carthage

> Ferramenta de gerenciamento de dependências para aplicativos Cocoa.
> Mais informações: <https://github.com/Carthage/Carthage>.

- Baixa a versão mais recente de todas as dependências mencionadas no Cartfile e realiza o build delas:

`carthage update`

- Atualiza as dependências, e faz build apenas para o iOS:

`carthage update --platform ios`

- Atualiza as dependências, sem realizar build de nenhuma delas:

`carthage update --no-build`

- Faz o download e rebuild da versão atual das dependências (sem atualizá-las):

`carthage bootstrap`

- Faz o rebuild de uma dependência específica:

`carthage build {{dependência}}`
