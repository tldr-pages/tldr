# terraform ոչնչացնել

> Ոչնչացնել բոլոր օբյեկտները, որոնք կառավարվում են Terraform կոնֆիգուրացիայից:.
> Լրացուցիչ տեղեկություններ. <https://developer.hashicorp.com/terraform/cli/commands/destroy>:.

- Ոչնչացնել բոլոր ենթակառուցվածքները ընթացիկ գրացուցակում.:

`terraform destroy`

- Ոչնչացնել ենթակառուցվածքը՝ բաց թողնելով ինտերակտիվ հաստատումը.:

`terraform destroy -auto-approve`

- Ոչնչացնել կոնկրետ ռեսուրս.:

`terraform destroy -target {{resource_type.resource_name[instance_index]}}`

- Նշեք արժեքներ մուտքագրման փոփոխականների համար.:

`terraform destroy -var '{{name1}}={{value1}}' -var '{{name2}}={{value2}}'`

- Նշեք արժեքներ ֆայլից մուտքագրված փոփոխականների համար.:

`terraform destroy -var-file {{path/to/file.tfvars}}`

- Ոչնչացնել ենթակառուցվածքը կոմպակտ նախազգուշացումներով.:

`terraform destroy -compact-warnings`
