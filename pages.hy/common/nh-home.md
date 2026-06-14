# nh տուն

> Կառավարեք և կազմաձևեք յուրաքանչյուր օգտատիրոջ միջավայրը՝ օգտագործելով Nix-ը:.
> `home-manager`-ի վերագործարկում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/nix-community/nh#usage>:.

- Կառուցեք և անցեք նշված Home Manager-ի փաթիլային կազմաձևին.:

`nh home switch {{path/to/flake}}`

- Թարմացրեք նշված Home Manager փաթիլների կազմաձևման բոլոր փաթիլային մուտքերը և կառուցեք այն.:

`nh home build {{path/to/flake}} {{[-u|--update]}}`

- Նիքս REPL-ում (Nix գնահատման միջավայր) բեռնեք Home Manager-ի նշված փաթիլային կոնֆիգուրացիան.:

`nh home repl {{path/to/flake}}`
