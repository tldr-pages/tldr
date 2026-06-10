# nix shell

> Սկսեք կեղև, որում առկա են նշված փաթեթները:.
> Տես նաև՝ `nix-shell`, `nix flake`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/nix3-shell>:.

- Սկսեք ինտերակտիվ վահանակ `nixpkgs`-ից որոշ փաթեթներով.:

`nix shell {{nixpkgs#pkg1 nixpkgs#packageSet.pkg2 ...}}`

- Սկսեք կեղև, որն ապահովում է փաթեթ `nixpkgs`-ի հին տարբերակից (21.05):

`nix shell {{nixpkgs/nixos-21.05#pkg}}`

- Սկսեք «լռելյայն փաթեթով» կեղևը ընթացիկ գրացուցակի փաթիլից՝ տպելով build տեղեկամատյանները, եթե որևէ կառուցում տեղի ունենա.:

`nix shell -L`

- Սկսեք պատյան փաթիլից փաթեթով GitHub-ում.:

`nix shell {{github:owner/repo#pkg}}`

- Գործարկեք հրամանը պատյանով փաթեթով.:

`nix shell {{nixpkgs#pkg}} -c {{some-cmd --someflag 'Some other arguments'}}`
