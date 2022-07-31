# codesign

> Criar e manipular assinaturas de código para macOS.
> Mais informações: <https://www.unix.com/man-page/osx/1/codesign/>.

- Assinar um aplicativo com um certificado:

`codesign --sign "{{Nome da Minha Empresa}}" {{caminho/para/App.app}}`

- Verificar o certificado de um aplicativo:

`codesign --verify {{caminho/para/App.app}}`
