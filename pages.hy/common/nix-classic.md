# nix դասական

> Դասական, կայուն ինտերֆեյս հզոր փաթեթների կառավարչի համար, որը փաթեթների կառավարումը դարձնում է հուսալի, վերարտադրելի և հռչակավոր:.
> Որոշ Nix հրամաններ, ինչպիսիք են `nix-build`, `nix-shell`, `nix-env` և `nix-store`-ն ունեն իրենց սեփական էջերը:.
> Տես նաև՝ `nix`:.
> Լրացուցիչ տեղեկություններ. <https://nixos.org/>:.

- Փաթեթ փնտրեք nixpkgs-ում իր անվան միջոցով.:

`nix-env {{[-qaP|--query --available --attr-path]}} {{search_term_regex}}`

- Սկսեք կեղևը նշված հասանելի փաթեթներով.:

`nix-shell {{[-p|--packages]}} {{pkg1 pkg2 pkg3 ...}}`

- Մշտապես տեղադրել որոշ փաթեթներ.:

`nix-env {{[-iA|--install --attr]}} {{nixpkgs.pkg1 nixpkgs.pkg2 ...}}`

- Ցույց տալ խանութի ուղու (փաթեթի) բոլոր կախվածությունները ծառի ձևաչափով.:

`nix-store {{[-q|--query]}} --tree /nix/store/{{checksum-package-version.ext}}`

- Թարմացրեք ալիքները (պահեստները).:

`nix-channel --update`

- Հեռացրեք չօգտագործված ուղիները Nix խանութից.:

`nix-collect-garbage`
