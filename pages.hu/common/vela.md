# vela

> Parancssori eszközök a Vela csővezetékhez. További információ: <https://go-vela.github.io/docs/reference/cli/>.

- A csővezeték indítása egy Git-ágból, commitból vagy tagből:

`vela add deployment --org {{organization}} --repo {{repository_name}} --target {{environment}} --ref {{branch|commit|refs/tags/git_tag}} --description "{{deploy_description}}"`

- Egy tárolóhely telepítéseinek listázása:

`vela get deployment --org {{organization}} --repo {{repository_name}}`

- Egy adott telepítés vizsgálata:

`vela view deployment --org {{organization}} --repo {{repository_name}} --deployment {{deployment_number}}`
