# nix պրոֆիլ

> Տեղադրեք, թարմացրեք և հեռացրեք փաթեթները Nix պրոֆիլներից:.
> Լրացուցիչ տեղեկություններ. <https://nix.dev/manual/nix/latest/command-ref/new-cli/nix3-profile.html>:.

- Տեղադրեք փաթեթներ nixpkgs-ից լռելյայն պրոֆիլում.:

`nix profile add {{nixpkgs#pkg1 nixpkgs#pkg2 ...}}`

- Տեղադրեք փաթեթ GitHub-ի փաթիլից հատուկ պրոֆիլում.:

`nix profile add {{github:owner/repo/pkg}} --profile {{path/to/directory}}`

- Ցուցակեք փաթեթները, որոնք ներկայումս տեղադրված են լռելյայն պրոֆիլում.:

`nix profile list`

- Հեռացրեք nixpkgs-ից տեղադրված փաթեթը լռելյայն պրոֆիլից՝ անունով.:

`nix profile remove {{legacyPackages.x86_64-linux.pkg}}`

- Թարմացրեք փաթեթները լռելյայն պրոֆիլում մինչև վերջին հասանելի տարբերակները.:

`nix profile upgrade --all`

- Հետ վերադարձնել (չեղարկել) լռելյայն պրոֆիլի վերջին գործողությունը.:

`nix profile rollback`
