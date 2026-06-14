# tuckr

> Dotfile կառավարիչը գրված է Rust-ով:.
> Տես նաև՝ `chezmoi`, `vcsh`, `homeshick`, `stow`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/RaphGL/Tuckr#usage>:.

- Ստուգեք dotfile կարգավիճակը.:

`tuckr status`

- Ավելացնել բոլոր dotfiles համակարգ.:

`tuckr add \*`

- Ավելացնել բոլոր dotfiles բացառությամբ նշված ծրագրերի:

`tuckr add \* -e {{program1}},{{program2}}`

- Հեռացրեք բոլոր dotfiles-ը համակարգից.:

`tuckr rm \*`

- Ավելացրեք ծրագրի dotfile և գործարկեք դրա տեղադրման սցենարը.:

`tuckr set {{program}}`
