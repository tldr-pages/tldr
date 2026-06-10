# nix-instantiate

> Ստեղծեք խանութի ածանցյալներ nix արտահայտություններից:.
> Տես նաև՝ `nix eval`:.
> Լրացուցիչ տեղեկություններ. <https://nix.dev/manual/nix/latest/command-ref/nix-instantiate.html>:.

- Նիքս ֆայլից ստեղծեք խանութի ածանցյալը.:

`nix-instantiate {{path/to/file.nix}}`

- Գնահատեք արտահայտությունը.:

`nix-instantiate --eval {{[-E|--expr]}} {{expression}}`

- Գնահատեք մեքենայական ընթեռնելի ելքով.:

`nix-instantiate --eval --xml {{[-E|--expr]}} {{expression}}`

- Հում ելքը, ֆունկցիայի ելքը պետք է լինի տող.:

`nix-instantiate --eval --raw {{[-E|--expr]}} {{expression}}`

- Գնահատեք Nix արտահայտությունը նշված ֆայլից.:

`nix-instantiate --eval {{path/to/file.nix}}`
