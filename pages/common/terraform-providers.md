# terraform providers

> Manage provider dependencies for Terraform configurations.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/providers>.

- Show providers required by the configuration:

`terraform providers`

- Update the dependency lock file for all providers:

`terraform providers lock`

- Update the lock file for multiple target platforms:

`terraform providers lock -platform={{linux_amd64}} -platform={{darwin_arm64}}`

- Mirror all required providers to a local directory:

`terraform providers mirror {{path/to/mirror_directory}}`

- Mirror providers for a specific platform:

`terraform providers mirror -platform={{linux_amd64}} {{path/to/mirror_directory}}`

- Print provider schemas in JSON format:

`terraform providers schema -json`

- Generate lock file entries using a filesystem mirror:

`terraform providers lock -fs-mirror={{path/to/mirror}}`

- Generate lock file entries using a network mirror:

`terraform providers lock -net-mirror={{https://mirror.example.com/providers/}}`
