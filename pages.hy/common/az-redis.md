# az redis

> Կառավարեք Redis-ի քեշերը:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/redis>:.

- Ստեղծեք Redis քեշի նոր օրինակ.:

`az redis create --location {{location}} {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}} --sku {{Basic|Premium|Standard}} --vm-size {{c0|c1|c2|c3|c4|c5|c6|p1|p2|p3|p4|p5}}`

- Թարմացրեք Redis քեշը.:

`az redis update {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}} --sku {{Basic|Premium|Standard}} --vm-size {{c0|c1|c2|c3|c4|c5|c6|p1|p2|p3|p4|p5}}`

- Արտահանեք Redis քեշում պահված տվյալները.:

`az redis export --container {{container}} --file-format {{file-format}} {{[-n|--name]}} {{name}} --prefix {{prefix}} {{[-g|--resource-group]}} {{resource_group}}`

- Ջնջել Redis քեշը.:

`az redis delete {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}} {{[-y|--yes]}}`
