# nix build

> Կառուցեք Nix արտահայտություն (հնարավորության դեպքում ներբեռնեք քեշից):.
> Տես նաև՝ `nix-build`, `nix flake`:.
> Լրացուցիչ տեղեկություններ. <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-build.html>:.

- Կառուցեք փաթեթ nixpkgs-ից՝ արդյունքը կապելով `./result`-ին:

`nix build {{nixpkgs#pkg}}`

- Կառուցեք փաթեթ ընթացիկ գրացուցակի փաթիլից՝ ցույց տալով կառուցման տեղեկամատյանները գործընթացում.:

`nix build {{[-L|--print-build-logs]}} {{.#pkg}}`

- Կառուցեք լռելյայն փաթեթը ինչ-որ գրացուցակի փաթիլից.:

`nix build {{path/to/directory}}`

- Կառուցեք փաթեթ՝ առանց `result` սիմհղումը կատարելու, փոխարենը տպելով խանութի ուղին դեպի `stdout`:

`nix build --no-link --print-out-paths`
