# jj git

> Գործարկել Git-ի հետ կապված հրամանները `jj` պահեստի համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.jj-vcs.dev/latest/cli-reference/#jj-git>:.

- Ստեղծեք նոր Git-ով ապահովված պահոց.:

`jj git init`

- Ստեղծեք նոր պահոց, որն ապահովված է Git պահեստի կլոնով.:

`jj git clone {{source}}`

- Վերցրեք Git հեռակառավարման վահանակից.:

`jj git fetch`

- Հրել բոլոր հետևված էջանիշները Git հեռակառավարման վրա.:

`jj git push`

- Տրված էջանիշը սեղմեք Git հեռակառավարման վրա.:

`jj git push {{[-b|--bookmark]}} {{bookmark}}`
