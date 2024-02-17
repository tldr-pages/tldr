# aws codeartifact

> Manage CodeArtifact repositories, domains, packages, package versions and assets.
> CodeArtifact is an artifact repository compatible with popular package managers and build tools like Maven, Gradle, npm, Yarn, Twine, pip, NuGet, and SwiftPM.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html>.

- List available domains for your AWS account:

`aws codeartifact list-domains`

- Generate credentials for a specific package manager:

`aws codeartifact login --tool {{npm|pip|twine}} --domain {{your_domain}} --repository {{repository_name}}`

- Get the endpoint URL of a CodeArtifact repository:

`aws codeartifact get-repository-endpoint --domain {{your_domain}} --repository {{repository_name}} --format {{npm|pypi|maven|nuget|generic}}`

- Display help:

`aws codeartifact help`

- Display help for a specific subcommand:

`aws codeartifact {{subcommand}} help`
