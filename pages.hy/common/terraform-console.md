# Terraform կոնսոլ

> Սկսեք ինտերակտիվ վահանակ Terraform արտահայտությունները գնահատելու համար:.
> Լրացուցիչ տեղեկություններ. <https://developer.hashicorp.com/terraform/cli/commands/console>:.

- Սկսեք ինտերակտիվ վահանակ արտահայտությունները գնահատելու համար.:

`terraform console`

- Գնահատեք ծրագրված վիճակի դեմ արտահայտությունները ներկայիս վիճակի փոխարեն.:

`terraform console -plan`

- Գնահատեք կոնկրետ արտահայտությունը ոչ ինտերակտիվ կերպով.:

`echo "{{expression}}" | terraform console`

- Նշեք արժեքներ մուտքագրման փոփոխականների համար.:

`terraform console -var '{{name1}}={{value1}}' -var '{{name2}}={{value2}}'`

- Նշեք արժեքներ ֆայլից մուտքագրված փոփոխականների համար.:

`terraform console -var-file {{path/to/file.tfvars}}`
