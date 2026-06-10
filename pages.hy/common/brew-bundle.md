# եփուկի փաթեթ

> Bundler Homebrew-ի, Homebrew Cask-ի և Mac App Store-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.brew.sh/Manpage#bundle-subcommand>:.

- Տեղադրեք փաթեթներ Brewfile-ից ընթացիկ ճանապարհով.:

`brew bundle`

- Տեղադրեք փաթեթներ կոնկրետ Brewfile-ից որոշակի ճանապարհով.:

`brew bundle --file {{path/to/file}}`

- Ստեղծեք Brewfile բոլոր տեղադրված փաթեթներից.:

`brew bundle dump`

- Տեղահանեք բոլոր բանաձևերը, որոնք նշված չեն Brewfile-ում.:

`brew bundle cleanup --force`

- Ստուգեք՝ արդյոք Brewfile-ում տեղադրելու կամ թարմացնելու բան կա.:

`brew bundle check`

- Թվարկեք Brewfile-ի բոլոր գրառումները.:

`brew bundle list --all`
