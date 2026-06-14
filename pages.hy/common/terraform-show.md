# Terraform շոու

> Կարդացեք և թողարկեք Terraform վիճակի կամ պլանի ֆայլը մարդու կողմից ընթեռնելի տեսքով:.
> Լրացուցիչ տեղեկություններ. <https://developer.hashicorp.com/terraform/cli/commands/show>:.

- Ցույց տալ ընթացիկ վիճակը.:

`terraform show`

- Ցույց տալ որոշակի պետական ֆայլ.:

`terraform show {{path/to/terraform.tfstate}}`

- Ցույց տալ որոշակի պլանի ֆայլ.:

`terraform show {{path/to/file.tfplan}}`

- Ելք JSON ձևաչափով.:

`terraform show -json`

- Ծրագրի ֆայլ թողարկեք JSON ձևաչափով.:

`terraform show -json {{path/to/file.tfplan}}`

- Գրեք ֆայլ առանց գունային կոդերի.:

`terraform show -no-color > {{path/to/file}}`
