#չեզմոյ

> Կառավարեք dotfiles-ը բազմաթիվ տարբեր մեքենաներում:.
> Տես նաև՝ `stow`, `tuckr`, `vcsh`, `homeshick`:.
> Լրացուցիչ տեղեկություններ. <https://www.chezmoi.io/reference/>:.

- Ստեղծեք `chezmoi`-ը՝ ստեղծելով Git պահոց `~/.local/share/chezmoi`-ում:

`chezmoi init`

- Տեղադրեք `chezmoi`-ը Git պահեստի առկա dotfiles-ից.:

`chezmoi init {{repository_url}}`

- Սկսեք հետևել մեկ կամ մի քանի կետային ֆայլերի.:

`chezmoi add {{path/to/dotfile1 path/to/dotfile2 ...}}`

- Թարմացրեք պահեստը տեղական փոփոխություններով.:

`chezmoi re-add {{path/to/dotfile1 path/to/dotfile2 ...}}`

- Խմբագրել հետևված կետային ֆայլի աղբյուրի վիճակը.:

`chezmoi edit {{path/to/dotfile_or_symlink}}`

- Տես սպասվող փոփոխությունները.:

`chezmoi diff`

- Կիրառել փոփոխությունները.:

`chezmoi apply`

- Քաշեք փոփոխությունները հեռավոր պահոցից և կիրառեք դրանք.:

`chezmoi update`
