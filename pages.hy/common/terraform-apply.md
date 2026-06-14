Կիրառել # տերրաֆորմ

> Ստեղծեք կամ թարմացրեք ենթակառուցվածքը Terraform-ի կազմաձևման ֆայլերի համաձայն:.
> Լրացուցիչ տեղեկություններ. <https://developer.hashicorp.com/terraform/cli/commands/apply>:.

- Ստեղծել կամ թարմացնել ենթակառուցվածքը.:

`terraform apply`

- Ստեղծեք կամ թարմացրեք ենթակառուցվածքը՝ բաց թողնելով ինտերակտիվ հաստատումը.:

`terraform apply -auto-approve`

- Կիրառեք պլանի ֆայլ.:

`terraform apply {{path/to/file.tfplan}}`

- Նշեք արժեքներ մուտքագրման փոփոխականների համար.:

`terraform apply -var '{{name1}}={{value1}}' -var '{{name2}}={{value2}}'`

- Նշեք արժեքներ ֆայլից մուտքագրված փոփոխականների համար.:

`terraform apply -var-file {{path/to/file.tfvars}}`

- Կիրառել փոփոխություններ կոնկրետ ռեսուրսում.:

`terraform apply -target {{resource_type.resource_name[instance_index]}}`

- Փոխարինեք որոշակի ռեսուրս.:

`terraform apply -replace {{resource_type.resource_name[instance_index]}}`

- Ոչնչացնել Terraform-ի կողմից կառավարվող ենթակառուցվածքը.:

`terraform apply -destroy`
