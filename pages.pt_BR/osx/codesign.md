# codesign

> Cria e manipula assinaturas de código para macOS.
> Mais informações: <https://www.unix.com/man-page/osx/1/codesign/>.

- Assina um aplicativo com um certificado:

`codesign --sign "{{Nome da Minha Empresa}}" {{caminho/para/App.app}}`

- Verifica o certificado de um aplicativo:

`codesign --verify {{caminho/para/App.app}}`
