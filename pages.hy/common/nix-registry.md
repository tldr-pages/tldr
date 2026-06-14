# nix ռեեստր

> Կառավարեք Nix flake ռեեստրը:.
> Տես նաև՝ `nix flake`:.
> Լրացուցիչ տեղեկություններ. <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-registry.html>:.

- Ամրացրեք `nixpkgs` տարբերակը վերին հոսանքի պահեստի ընթացիկ տարբերակին.:

`nix registry pin {{nixpkgs}}`

- Ամրացրեք մուտքը մասնաճյուղի վերջին տարբերակին կամ GitHub պահեստի որոշակի վերանայմանը.:

`nix registry pin {{entry}} {{github:owner/repo/branch_or_revision}}`

- Ավելացրեք նոր գրառում, որը միշտ մատնանշում է GitHub պահեստի վերջին տարբերակը՝ ինքնաբերաբար թարմացվող:

`nix registry add {{entry}} {{github:owner/repo}}`

- Հեռացնել գրանցամատյանի գրառումը.:

`nix registry remove {{entry}}`

- Տեսեք փաստաթղթերը, թե ինչ են Nix flake ռեգիստրները.:

`nix registry --help`
