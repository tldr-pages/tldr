# az սկավառակ

> Կառավարեք Azure կառավարվող սկավառակները:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/disk>:.

- Ստեղծեք կառավարվող սկավառակ.:

`az disk create {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{disk_name}} {{[-z|--size-gb]}} {{size_in_gb}}`

- Ցուցակեք կառավարվող սկավառակները ռեսուրսների խմբում.:

`az disk list {{[-g|--resource-group]}} {{resource_group}}`

- Ջնջել կառավարվող սկավառակը.:

`az disk delete {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{disk_name}}`

- Տրամադրել կարդալու կամ գրելու մուտք դեպի կառավարվող սկավառակ (արտահանման համար).:

`az disk grant-access {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{disk_name}} {{[--access|--access-level]}} {{Read|Write}} --duration-in-seconds {{seconds}}`

- Թարմացրեք սկավառակի չափը.:

`az disk update {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{disk_name}} {{[-z|--size-gb]}} {{new_size_in_gb}}`
