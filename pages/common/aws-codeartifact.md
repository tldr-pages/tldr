# aws codeartifact

> CLI for AWS CodeArtifact.
> CodeArtifact allows you to store artifacts using popular package managers and build tools like Maven, Gradle, npm, Yarn, Twine, pip, NuGet, and SwiftPM.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html>.

- List available domains for your AWS account:

`aws codeartifact list-domains`

- Generate credentials for a specific package manager (e.g.: npm, pip):

`aws codeartifact login --tool {{package_manager}} --domain {{your_domain}} --repository {{repository_name}}`

- Get the endpoint URL of a CodeArtifact repository:

`aws codeartifact get-repository-endpoint --domain {{your_domain}} --repository {{repository_name}} --format {{npm|pypi|maven|nuget|generic}}`

- Show list of all available CodeArtifact commands:

`aws codeartifact help`

- Show help for specific EC2 subcommand:

`aws ec2 {{subcommand}} help`
