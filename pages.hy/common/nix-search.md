# nix որոնում

> Փնտրեք փաթեթներ Nix փաթիլում:.
> Լրացուցիչ տեղեկություններ. <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-search.html>:.

- Փնտրեք `nixpkgs` փաթեթը՝ հիմնված դրա անվան կամ նկարագրության վրա.:

`nix search {{nixpkgs}} {{search_term}}`

- Ցույց տալ փաթեթի նկարագրությունը nixpkgs-ից.:

`nix search {{nixpkgs#pkg}}`

- Ցույց տալ բոլոր փաթեթները, որոնք հասանելի են փաթիլից github-ում.:

`nix search {{github:owner/repo}}`
