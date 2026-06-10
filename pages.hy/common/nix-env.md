# nix-env

> Շահարկել կամ հարցումներ կատարել Nix-ի օգտատերերի միջավայրերը:.
> Լրացուցիչ տեղեկություններ. <https://nix.dev/manual/nix/stable/command-ref/nix-env.html>:.

- Նշեք բոլոր տեղադրված փաթեթները.:

`nix-env {{[-q|--query]}}`

- Տեղադրված փաթեթների հարցում (`regex` աջակցվում է).:

`nix-env {{[-q|--query]}} {{search_pattern}}`

- Հարցրեք հասանելի փաթեթները Nixpkgs ռեեստրից.:

`nix-env {{[-qa|--query --available]}} {{search_pattern}}`

- Տեղադրեք փաթեթ Nixpkgs ռեեստրից.:

`nix-env {{[-iA|--install --attr]}} nixpkgs.{{pkg_name}}`

- Տեղադրեք փաթեթ հատուկ URL-ից.:

`nix-env {{[-i|--install]}} {{pkg_name}} {{[-f|--file]}} {{example.com}}`

- Ապատեղադրել փաթեթը.:

`nix-env {{[-e|--uninstall]}} {{pkg_name}}`

- Թարմացրեք փաթեթը.:

`nix-env {{[-u|--upgrade]}} {{pkg_name}}`

- Ստացեք օգտագործման օգնություն կոնկրետ գործողության համար (`--install`, `--upgrade` և այլն):

`nix-env --help --{{option_name}}`
