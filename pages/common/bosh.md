# bosh

> Command-line tool to deploy and manage the bosh director.
> More information: <https://bosh.io/docs/cli-v2/>.

- Create local alias for director:

`bosh alias-env {{environment_name}} -e {{ip_address|url}} --ca-cert {{ca_certificate}}`

- List environments:

`bosh environments`

- Log in to the director:

`bosh login -e {{environment}} `

- List deployments:

`bosh -e {{environment}} deployments`

- List environment virtual machines:

`bosh -e {{environment}} vms -d {{deployment}}`

- Ssh into virtual machine:

`bosh -e {{environment}} ssh {{virtual_machine}} -d {{deployment}}`

- Upload stemcell:

`bosh -e {{environment}} upload-stemcell {{stemcell_file|url}}`

- Show current cloud config:

`bosh -e {{environment}} cloud-config`
