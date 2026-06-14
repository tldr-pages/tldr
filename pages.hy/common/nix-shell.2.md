# nix-shell

> Սկսեք ինտերակտիվ պատյան, որը հիմնված է Nix արտահայտության վրա:.
> Տես նաև՝ `nix shell.3`:.
> Լրացուցիչ տեղեկություններ. <https://nix.dev/manual/nix/stable/command-ref/nix-shell.html>:.

- Սկսեք nix արտահայտությունով `shell.nix`-ում կամ `default.nix`-ում ընթացիկ գրացուցակում:

`nix-shell`

- Գործարկեք shell հրամանը ոչ ինտերակտիվ վահանակում և դուրս եկեք.:

`nix-shell --run "{{command}} {{argument1 argument2 ...}}"`

- Սկսեք արտահայտությամբ `default.nix`-ով ընթացիկ գրացուցակում.:

`nix-shell {{default.nix}}`

- Սկսեք nixpkgs-ից բեռնված փաթեթներից.:

`nix-shell {{[-p|--packages]}} {{package1 package2 ...}}`

- Սկսեք փաթեթներից, որոնք բեռնված են հատուկ nixpkgs վերանայումից.:

`nix-shell {{[-p|--packages]}} {{package1 package2 ...}} {{[-I|--include]}} nixpkgs={{https://github.com/NixOS/nixpkgs/archive/nixpkgs_revision.tar.gz}}`

- Գնահատեք ֆայլի մնացած մասը հատուկ թարգմանչի մեջ՝ `#!-scripts`-ում օգտագործելու համար (տես <https://nixos.org/manual/nix/stable/#use-as-a-interpreter>):

`nix-shell -i {{interpreter}} {{[-p|--packages]}} {{package1 package2 ...}}`
