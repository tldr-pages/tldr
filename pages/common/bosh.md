# bosh

> Deploy and manage the BOSH director.
> More information: <https://bosh.io/docs/cli-v2/>.

- Create local alias for director in a specific [e]nvironment:

`bosh alias-env {{environment_name}} -e {{ip_address|URL}} --ca-cert {{ca_certificate}}`

- List environments:

`bosh environments`

- Log in to the director:

`bosh login -e {{environment}}`

- List deployments:

`bosh -e {{environment}} deployments`

- List environment virtual machines in a [d]eployment:

`bosh -e {{environment}} vms -d {{deployment}}`

- SSH into virtual machine:

`bosh -e {{environment}} ssh {{virtual_machine}} -d {{deployment}}`

- Upload stemcell:

`bosh -e {{environment}} upload-stemcell {{stemcell_file|url}}`

- Show current cloud config:

`bosh -e {{environment}} cloud-config`
