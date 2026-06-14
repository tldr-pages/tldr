# nix flake show

> Ցուցադրել փաթիլով տրամադրված արդյունքները:.
> Լրացուցիչ տեղեկություններ. <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-flake-show.html>:.

- Ցույց տալ փաթիլների բոլոր ելքերը ընթացիկ գրացուցակում.:

`nix flake show`

- Ցույց տվեք փաթիլների բոլոր ելքերը GitHub-ում և տպեք արդյունքը որպես json մեկ տողի վրա.:

`nix flake show {{github:owner/repo}} --json --no-pretty`

- Ցուցադրել փաթիլի բոլոր `legacyPackages` ելքերը GitHub-ում և տպել ելքը որպես բազմատող նահանջ json:

`nix flake show {{github:owner/repo}} --json --pretty --legacy`

- Թվարկեք բոլոր հասանելի փաթիլային ձևանմուշները `nix flake init`-ի համար.:

`nix flake show templates`
