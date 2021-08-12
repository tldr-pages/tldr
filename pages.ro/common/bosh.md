# bosh

> Instrument de linie de comandă pentru a implementa și gestiona directorul bosh.
> Mai multe informaţii: <https://bosh.io/docs/cli-v2/>

- Creați alias local pentru director:

`bosh alias-env {{environment_name}} -e {{ip_address|url}} --ca-cert {{ca_certificate}}`

- Lista mediilor:

`bosh environments`

- Conectați-vă la director:

`bosh login -e {{environment}} `

- Implementările listei:

`bosh -e {{environment}} deployments`

- Lista mașinilor virtuale de mediu:

`bosh -e {{environment}} vms -d {{deployment}}`

- Ssh în mașină virtuală:

`bosh -e {{environment}} ssh {{virtual_machine}} -d {{deployment}}`

- Încarcă stemcell:

`bosh -e {{environment}} upload-stemcell {{stemcell_file|url}}`

- Afișează configurarea norului curent:

`bosh -e {{environment}} cloud-config`
