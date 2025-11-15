# codesign

> Cria e manipula assinaturas de código para macOS.
> Mais informações: <https://keith.github.io/xcode-man-pages/codesign.1.html>.

- Assina um aplicativo com um certificado:

`codesign --sign "{{Nome da Minha Empresa}}" {{caminho/para/App.app}}`

- Verifica o certificado de um aplicativo:

`codesign --verify {{caminho/para/App.app}}`
