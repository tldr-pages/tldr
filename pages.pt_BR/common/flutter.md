# flutter

> SDK livre e open source do Google para desenvolvimento de aplicativos mobile cross-platform.
> Mais informações: <https://github.com/flutter/flutter/wiki/The-flutter-tool>.

- Mostra ajuda sobre algum comando específico:

`flutter help {{comando}}`

- Verifica se todas as ferramentas externas necessárias estão instaladas:

`flutter doctor`

- Lista ou muda o channel do Flutter:

`flutter channel {{stable|beta|dev|master}}`

- Executa o projeto Flutter em todos os emuladores ativos ou devices conectados:

`flutter run -d all`

- Instala todas as dependências definidas no `pubspec.yaml`:

`flutter pub get`

- Executa todos os testes no terminal a partir da raíz do projeto:

`flutter test {{test/example_test.dart}}`

- Builda APK de release direcionado aos mais modernos smartphones:

`flutter build apk --target-platform {{android-arm}},{{android-arm64}}`
