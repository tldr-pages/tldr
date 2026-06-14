# vcsh

> Տարբերակների վերահսկման համակարգ տնային գրացուցակի համար՝ օգտագործելով Git պահեստները:.
> Տես նաև՝ `chezmoi`, `stow`, `tuckr`, `homeshick`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/vcsh>:.

- Նախաձեռնել (դատարկ) պահեստ.:

`vcsh init {{repository_name}}`

- Կլոնավորեք պահեստը հատուկ գրացուցակի անվան մեջ.:

`vcsh clone {{git_url}} {{repository_name}}`

- Թվարկեք բոլոր կառավարվող պահեստները.:

`vcsh list`

- Կատարեք Git հրամանը կառավարվող պահեստում.:

`vcsh {{repository_name}} {{git_command}}`

- Հրել/քաշել բոլոր կառավարվող պահեստները դեպի/հեռակառավարվող սարքերից.:

`vcsh {{push|pull}}`

- Գրեք հատուկ `.gitignore` ֆայլ կառավարվող պահեստի համար.:

`vcsh write-gitignore {{repository_name}}`
