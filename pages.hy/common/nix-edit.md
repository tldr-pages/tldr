# nix խմբագրում

> Բացեք Nix փաթեթի Nix արտահայտությունը `$EDITOR`-ում:.
> Լրացուցիչ տեղեկություններ. <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-edit.html>:.

- Բացեք փաթեթի Nix արտահայտության աղբյուրը nixpkgs-ից ձեր `$EDITOR`-ում:

`nix edit {{nixpkgs#pkg}}`

- Թափել փաթեթի աղբյուրը `stdout`:

`EDITOR=cat nix edit {{nixpkgs#pkg}}`
