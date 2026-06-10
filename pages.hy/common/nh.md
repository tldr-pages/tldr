# nh

> Ժամանակակից օգտակար գործիք Nix/NixOS էկոհամակարգի համար:.
> Որոշ ենթահրամաններ, ինչպիսիք են `os`, `home`, `clean`, `search`, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/nix-community/nh#usage>:.

- Կառուցեք և անցեք նշված NixOS փաթիլային կազմաձևին.:

`nh os switch {{path/to/flake}}`

- Կառուցեք և անցեք նշված Home Manager-ի փաթիլային կազմաձևին.:

`nh home switch {{path/to/flake}}`

- Կառուցեք և անցեք nix-darwin flake կոնֆիգուրացիայի.:

`nh darwin switch {{path/to/flake}} {{[-H|--hostname]}} {{host}}`

- Հավաքեք բոլոր աղբն ու աղբը Nix խանութից.:

`nh clean all {{[-a|--ask]}}`

- Փաթեթ փնտրեք Nixpkgs-ում.:

`nh search {{name}}`

- Ստեղծեք կեղևի լրացումներ նշված կեղևի համար.:

`nh completions {{shell}}`
