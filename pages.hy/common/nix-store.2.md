# nix-խանութ

> Շահարկել կամ հարցումներ կատարել Nix խանութում:.
> Տես նաև՝ `nix store.3`:.
> Լրացուցիչ տեղեկություններ. <https://nix.dev/manual/nix/stable/command-ref/nix-store.html>:.

- Հավաքեք աղբը, օրինակ՝ չօգտագործված ուղիների հեռացումը.:

`nix-store --gc`

- Կոշտ կապակցված նույնական ֆայլերը միասին՝ տարածքի օգտագործումը նվազեցնելու համար.:

`nix-store --optimise`

- Ջնջել հատուկ խանութի ուղին (պետք է չօգտագործված լինի).:

`nix-store --delete /nix/store/{{checksum-package-version.ext}}`

- Ցույց տալ խանութի ուղու (փաթեթի) բոլոր կախվածությունները ծառի ձևաչափով.:

`nix-store {{[-q|--query]}} --tree /nix/store/{{checksum-package-version.ext}}`

- Հաշվեք որոշակի խանութի ուղու ընդհանուր չափը բոլոր կախվածություններով.:

`du {{[-cLsh|--total --dereference --summarize --human-readable]}} $(nix-store {{[-q|--query]}} --references /nix/store/{{checksum-package-version.ext}})`

- Ցույց տալ որոշակի խանութի ուղու բոլոր կախյալներին.:

`nix-store {{[-q|--query]}} --referrers /nix/store/{{checksum-package-version.ext}}`
