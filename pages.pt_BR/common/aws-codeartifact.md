# aws codeartifact

> Gerencia repositórios, domínios, pacotes, versões de pacotes e ativos do CodeArtifact.
> O CodeArtifact é um repositório de artefatos compatível com gerenciadores de pacotes populares e ferramentas de construção como Maven, Gradle, npm, Yarn, Twine, pip, NuGet e SwiftPM.
> Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html>.

- Lista domínios disponíveis para a sua conta da AWS:

`aws codeartifact list-domains`

- Gera credenciais para um gerenciador de pacote específico:

`aws codeartifact login --tool {{npm|pip|twine}} --domain {{seu_domínio}} --repository {{nome_do_repositório}}`

- Recupera a URL do endpoint de um repositório do CodeArtifact:

`aws codeartifact get-repository-endpoint --domain {{seu_domínio}} --repository {{nome_do_repositório}} --format {{npm|pypi|maven|nuget|generic}}`

- Exibe ajuda:

`aws codeartifact help`

- Exibe ajuda para um subcomando específico:

`aws codeartifact {{subcomando}} help`
