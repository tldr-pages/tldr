# nixpkgs-ակնարկ

> Վերանայեք ձգման հարցումները NixOS փաթեթների պահոցում (nixpkgs):.
> Հաջող կառուցումից հետո գործարկվում է `nix-shell` բոլոր ներկառուցված փաթեթներով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Mic92/nixpkgs-review#usage>:.

- Կառուցեք փոփոխված փաթեթներ նշված ձգման հարցումով.:

`nixpkgs-review pr {{pr_number|pr_url}}`

- Կառուցեք փոփոխված փաթեթներ և տեղադրեք մեկնաբանություն զեկույցով (պահանջվում է թոքենի կարգավորում `hub`, `gh` կամ `$GITHUB_TOKEN` միջավայրի փոփոխականում):

`nixpkgs-review pr --post-result {{pr_number|pr_url}}`

- Կառուցեք փոփոխված փաթեթներ և տպեք հաշվետվություն.:

`nixpkgs-review pr --print-result {{pr_number|pr_url}}`

- Կառուցեք փոփոխված փաթեթներ տեղական կոմիտում.:

`nixpkgs-review rev {{HEAD}}`

- Կառուցեք փոփոխված փաթեթներ, որոնք դեռ չեն կատարվել.:

`nixpkgs-review wip`

- Կառուցեք փոփոխված փաթեթներ, որոնք բեմադրված են.:

`nixpkgs-review wip --staged`
