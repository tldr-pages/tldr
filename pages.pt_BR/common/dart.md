# dart

> A ferramenta para gerenciar projetos Dart.
> Mais informações: <https://dart.dev/tools/dart-tool>.

- Inicializa um novo projeto Dart em um diretório com o mesmo nome:

`dart create {{nome_do_projeto}}`

- Executa um arquivo Dart:

`dart run {{caminho/para/arquivo.dart}}`

- Baixa as dependências do projeto atual:

`dart pub get`

- Executa testes de unidade para o projeto atual:

`dart test`

- Atualiza as dependências de um projeto desatualizado para oferecer suporte à segurança nula:

`dart pub upgrade --null-safety`

- Compila um arquivo Dart para um binário nativo:

`dart compile exe {{caminho/para/arquivo.dart}}`
