# nix

> Փաթեթների հզոր կառավարիչ, որը փաթեթների կառավարումը դարձնում է հուսալի, վերարտադրելի և հռչակավոր:.
> `nix`-ի որոշ գործառույթներ (`nix command`, `flakes` և այլն) փորձնական են և պահանջում են միացնել փորձնական գործառույթները:.
> Որոշ ենթահրամաններ, ինչպիսիք են `build`, `develop`, `flake`, `registry`, `profile`, `search`, `repl`, __1_IN_CO, `edit`, `why-depends` և այլն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Տես նաև՝ `nix classic`:.
> Լրացուցիչ տեղեկություններ. <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix>:.

- Միացնել `nix` հրամանը.:

`mkdir {{[-p|--parents]}} ~/.config/nix; echo 'experimental-features = nix-command flakes' > ~/.config/nix/nix.conf`

- Փաթեթ փնտրեք nixpkgs-ում դրա անվան կամ նկարագրության միջոցով.:

`nix search nixpkgs {{search_term}}`

- Սկսեք կեղևը նշված փաթեթներով nixpkgs հասանելի:

`nix shell {{nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...}}`

- Տեղադրեք որոշ փաթեթներ nixpkgs-ից մշտապես.:

`nix profile install {{nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...}}`

- Հեռացրեք չօգտագործված ուղիները Nix խանութից՝ տարածք ազատելու համար.:

`nix store gc`

- Սկսեք ինտերակտիվ միջավայր՝ Nix արտահայտությունները գնահատելու համար.:

`nix repl`

- Ցուցադրել օգնություն կոնկրետ ենթահրամանի համար.:

`nix help {{subcommand}}`
