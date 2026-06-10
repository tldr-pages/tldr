# թափառաշրջիկ սշ

> SSH-ը գործարկվող Vagrant մեքենայի մեջ:.
> Տես նաև՝ `vagrant`:.
> Լրացուցիչ տեղեկություններ. <https://developer.hashicorp.com/vagrant/docs/cli/ssh>:.

- SSH ընթացիկ գրացուցակում աշխատող մեքենայի մեջ.:

`vagrant ssh`

- Թիրախավորեք գործող մեքենան անունով կամ ID-ով.:

`vagrant ssh {{name|id}}`

- Կատարեք SSH հրաման և դուրս եկեք.:

`vagrant ssh {{[-c|--command]}} {{ssh_command}}`

- SSH առանց նույնականացման՝ նույնականացումը թողնելով օգտագործողին.:

`vagrant ssh {{[-p|--plain]}}`
