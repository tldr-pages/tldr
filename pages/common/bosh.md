# bosh

> Deploy and manage the BOSH director.
> More information: <https://bosh.io/docs/cli-v2/>.

- Create local alias for director in a specific environment:

`bosh alias-env {{environment_name}} {{[-e|--environment]}} {{ip_address|URL}} --ca-cert {{ca_certificate}}`

- List environments:

`bosh environments`

- Log in to the director:

`bosh login {{[-e|--environment]}} {{environment}}`

- List deployments:

`bosh {{[-e|--environment]}} {{environment}} deployments`

- List environment virtual machines in a deployment:

`bosh {{[-e|--environment]}} {{environment}} vms {{[-d|--deployment]}} {{deployment}}`

- SSH into virtual machine:

`bosh {{[-e|--environment]}} {{environment}} ssh {{virtual_machine}} {{[-d|--deployment]}} {{deployment}}`

- Upload stemcell:

`bosh {{[-e|--environment]}} {{environment}} upload-stemcell {{stemcell_file|url}}`

- Show current cloud config:

`bosh {{[-e|--environment]}} {{environment}} cloud-config`
