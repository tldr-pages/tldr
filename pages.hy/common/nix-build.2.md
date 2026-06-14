# nix-build

> Կառուցեք Nix արտահայտություն:.
> Տես նաև՝ `nix build.3`:.
> Լրացուցիչ տեղեկություններ. <https://nix.dev/manual/nix/stable/command-ref/nix-build.html>:.

- Կառուցեք Nix արտահայտություն.:

`nix-build '<nixpkgs>' {{[-A|--attr]}} {{firefox}}`

- Ստեղծեք ավազապատ Nix արտահայտություն (ոչ NixOS-ի վրա).:

`nix-build '<nixpkgs>' {{[-A|--attr]}} {{firefox}} --option sandbox true`
