# terraform init

> Initialize a new or existing Terraform working directory.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/init>.

- Initialize the current working directory:

`terraform init`

- Initialize and upgrade modules and providers to the latest allowed versions:

`terraform init -upgrade`

- Initialize and reconfigure the backend, ignoring any saved configuration:

`terraform init -reconfigure`

- Initialize and reconfigure the backend, attempting to migrate any existing state:

`terraform init -migrate-state`

- Initialize with additional backend configuration:

`terraform init -backend-config '{{key}}={{value}}'`

- Initialize without backend or HCP Terraform initialization:

`terraform init -backend=false`

- Initialize without interactive prompts (useful for automation):

`terraform init -input=false`

- Initialize with the dependency lockfile mode set to readonly:

`terraform init -lockfile readonly`
