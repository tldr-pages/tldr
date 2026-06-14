# nix խանութ

> Շահարկել Nix խանութը:.
> Տես նաև՝ `nix-store`:.
> Լրացուցիչ տեղեկություններ. <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-store.html>:.

- Հավաքեք աղբը, այսինքն՝ հեռացրեք չօգտագործված ուղիները՝ տարածքի օգտագործումը նվազեցնելու համար.:

`nix store gc`

- Կոշտ կապակցված նույնական ֆայլերը միասին՝ տարածքի օգտագործումը նվազեցնելու համար.:

`nix store optimise`

- Ջնջել հատուկ խանութի ուղին (պետք է չօգտագործված լինի).:

`nix store delete /nix/store/{{checksum-package-version.ext}}`

- Թվարկեք խանութի ուղու բովանդակությունը հեռավոր խանութում.:

`nix store --store {{https://cache.nixos.org}} ls /nix/store/{{checksum-package-version.ext}}`

- Ցույց տալ տարբերակների տարբերությունները երկու խանութի ուղիների միջև՝ իրենց համապատասխան կախվածությամբ.:

`nix store diff-closures /nix/store/{{checksum-package-version.ext}} /nix/store/{{checksum-package-version.ext}}`
