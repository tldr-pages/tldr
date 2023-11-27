# aws codeartifact

> Interface de linha de comando para o AWS CodeArtifact.
> O CodeArtifact permite armazenar artefatos usando gerenciadores de pacotes populares e criar ferramentas como Maven, Gradle, npm, Yarn, Twine, pip e NuGet.
> Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html>.

- Lista domínios disponíveis para a sua conta da AWS:

`aws codeartifact list-domains`

- Gera credenciais para um gerenciador de pacote específico (p.e.: npm, pip):

`aws codeartifact login --tool {{gerenciador_de_pacotes}} --domain {{seu_domínio}} --repository {{nome_do_repositório}}`

- Recupera a URL do endpoint de um repositório do CodeArtifact:

`aws codeartifact get-repository-endpoint --domain {{seu_domínio}} --repository {{nome_do_repositório}} --format {{npm|pypi|maven|nuget|generic}}`

- Lista todos os comandos disponíveis para o CodeArtifact:

`aws codeartifact help`

- Exibe ajuda específica para um subcomando do CodeArtifact:

`aws ec2 {{subcommand}} help`
