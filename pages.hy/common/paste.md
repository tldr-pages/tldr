#մածուկ

> Միավորել ֆայլերի տողերը:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/paste-invocation.html>:.

- Միացրեք բոլոր տողերը մեկ տողի մեջ՝ օգտագործելով `TAB` որպես սահմանազատող:

`paste {{[-s|--serial]}} {{path/to/file}}`

- Միացրեք բոլոր տողերը մեկ տողի մեջ՝ օգտագործելով նշված սահմանազատիչը.:

`paste {{[-s|--serial]}} {{[-d|--delimiters]}} {{delimiter}} {{path/to/file}}`

- Միավորել երկու ֆայլ կողք կողքի, յուրաքանչյուրն իր սյունակում, օգտագործելով `TAB` որպես սահմանազատող:

`paste {{path/to/file1}} {{path/to/file2}}`

- Միավորել երկու ֆայլ կողք կողքի, յուրաքանչյուրն իր սյունակում, օգտագործելով նշված սահմանազատիչը.:

`paste {{[-d|--delimiters]}} {{delimiter}} {{path/to/file1}} {{path/to/file2}}`

- Միավորել երկու ֆայլ, այլընտրանքային տողերով.:

`paste {{[-d|--delimiters]}} '\n' {{path/to/file1}} {{path/to/file2}}`
