# flutter

> Flutter é o kit de ferramentas de IU do Google para construir aplicativos bonitos e compilados nativamente para dispositivos móveis, web, desktop e incorporados a partir de uma única base de código.
> Para mais informações: <https://github.com/flutter/flutter/wiki/The-flutter-tool>.

- Mostrar ajuda sobre algum comando específico:

`flutter help {{command}}`

- Verificar se todas as ferramentas externas necessárias estão instaladas:

`flutter doctor`

- Listar ou mudar o channel do Flutter

`flutter channel {{stable|beta|dev|master}}`

- Executar projeto Flutter em todos os emuladores ativos ou devices conectados:

`flutter run -d all`

- Instalar todas as dependências definidas no `pubspec.yaml`:

`flutter pub get`

- Executar todos os testes {{ou executar testes de um arquivo específico}}

`flutter test {{test/example_test.dart}}`

- Buildar APK de release (Android):

`flutter build apk --target-platform {{android-arm}},{{android-arm64}}`
