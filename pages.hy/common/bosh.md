#բոշ

> Տեղակայել և կառավարել BOSH տնօրենին:.
> Լրացուցիչ տեղեկություններ. <https://bosh.io/docs/cli-v2/>:.

- Ստեղծեք տեղական կեղծանուններ ռեժիսորի համար կոնկրետ միջավայրում.:

`bosh alias-env {{environment_name}} {{[-e|--environment]}} {{ip_address|url}} --ca-cert {{ca_certificate}}`

- Ցուցակեք միջավայրերը.:

`bosh environments`

- Մուտք գործեք տնօրեն.:

`bosh login {{[-e|--environment]}} {{environment}}`

- Ցուցակ տեղակայումները.:

`bosh {{[-e|--environment]}} {{environment}} deployments`

- Թվարկեք միջավայրի վիրտուալ մեքենաները տեղակայման մեջ.:

`bosh {{[-e|--environment]}} {{environment}} vms {{[-d|--deployment]}} {{deployment}}`

- SSH վիրտուալ մեքենայի մեջ.:

`bosh {{[-e|--environment]}} {{environment}} ssh {{virtual_machine}} {{[-d|--deployment]}} {{deployment}}`

- Վերբեռնեք ցողունային բջիջ.:

`bosh {{[-e|--environment]}} {{environment}} upload-stemcell {{stemcell_file|url}}`

- Ցույց տալ ընթացիկ ամպի կազմաձևը.:

`bosh {{[-e|--environment]}} {{environment}} cloud-config`
