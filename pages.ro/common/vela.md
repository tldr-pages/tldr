# vela

> Instrumente de linie de comandă pentru conducta Vela.
> Mai multe informaţii: <https://go-vela.github.io/docs/reference/cli/>

- Declanșați o conductă pentru a rula dintr-o ramură Git, comite sau etichetați

`vela add deployment --org {{organization}} --repo {{repository_name}} --target {{environment}} --ref {{branch|commit|refs/tags/git_tag}} --description "{{deploy_description}}"`

- Listează implementările pentru un depozit:

`vela get deployment --org {{organization}} --repo {{repository_name}}`

- Inspectaţi o implementare specifică:

`vela view deployment --org {{organization}} --repo {{repository_name}} --deployment {{deployment_number}}`
