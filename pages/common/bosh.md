# bosh

> Command line tool to deploy and manage the bosh director.

- Create local alias for director:

`bosh alias-env {{environment-name}} -e {{ip address or url}} --ca-cert {{ca_certificate}}`

- List environments:

`bosh environments`

- Login to the director:

`bosh login -e {{environment}} `

- List deployments:

`bosh -e {{environment}} deployments`

- List environment virtual machines:

`bosh -e {{environment}} vms -d {{deployment}}`

- Ssh into virtual machine:

`bosh -e {{environment}} ssh {{virtual machine}} -d {{deployment}}`

- Upload stemcell:

`bosh -e {{environment}} upload-stemcell {{stemcell file or url}}`

- Show current cloud config:

`bosh -e {{environment}} cloud-config`
