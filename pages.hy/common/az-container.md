# az կոնտեյներ

> Կառավարեք Azure կոնտեյների օրինակները:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/container>:.

- Ստեղծեք կոնտեյներ կոնտեյների խմբում.:

`az container create {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{name}} --image {{image_name}} {{[-os|--os-type]}} {{windows|linux}} --cpu {{number_of_cpu_cores}} --memory {{memory_in_GB}}`

- Կատարեք հրաման կոնտեյների խմբի գործող կոնտեյների ներսից.:

`az container exec {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{container_group_name}} --exec-command "{{command}}"`

- Ուսումնասիրեք կոնտեյների տեղեկամատյանները կոնտեյների խմբի մեջ.:

`az container logs {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Ստացեք կոնտեյների խմբի մանրամասները.:

`az container show {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Սկսեք բոլոր բեռնարկղերը կոնտեյների խմբի մեջ.:

`az container start {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Դադարեցրեք բոլոր բեռնարկղերը կոնտեյների խմբի մեջ.:

`az container stop {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Ջնջել կոնտեյների խումբը.:

`az container delete {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`
