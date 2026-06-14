# nix ինչու-կախված է

> Ցույց տալ, թե ինչու է փաթեթը կախված մեկ այլ փաթեթից:.
> Լրացուցիչ տեղեկություններ. <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-why-depends.html>:.

- Ցույց տվեք, թե ինչու է ներկայումս գործող NixOS համակարգը պահանջում խանութի որոշակի ուղի.:

`nix why-depends {{/run/current-system}} /nix/store/{{checksum-package-version.ext}}`

- Ցույց տվեք, թե ինչու է nixpkgs փաթեթը պահանջում մեկ այլ փաթեթ՝ որպես կառուցման ժամանակի կախվածություն.:

`nix why-depends --derivation {{nixpkgs#dependent}} {{nixpkgs#dependency}}`
