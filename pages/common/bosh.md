# bosh

> Cli tool to deploy and manage the bosh director

- Deploy the director:

`bosh create-env {{bosh.yml}} --state={{state.json}} --vars-store={{creds.yml}} -v {{custparam}}`

- Create local alias for director:

`bosh alias-env {{name}} -e {{192.168.1.123}} --ca-cert {{$(bosh int ./creds.yml --path /director_ssl/ca)}}`

- Login to the director:

`bosh login -e {{environment}} --client={{username}} --client-secret={{password}}`

- List environments:

`bosh environments`

- List environment vm's:

`bosh -e {{environment}} vms`

- List deployments:

`bosh -e {{environment}} deployments`

- Upload stemcell:

`bosh -e {{environment}} upload-stemcell {{stemcell.tgz|https://bosh.io/d/stemcells/bosh-warden-boshlite-ubuntu-trusty-go_agent}}`

- Upload cloud config:

`bosh -e {{environment }}update-cloud-config {{cloud.yml}}`
