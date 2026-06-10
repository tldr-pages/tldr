#քեյթ

> KDE-ի առաջադեմ տեքստային խմբագրիչ:.
> Լրացուցիչ տեղեկություններ. <https://docs.kde.org/stable/en/kate/kate/fundamentals.html#starting-from-the-command-line>:.

- Բացեք հատուկ ֆայլեր.:

`kate {{path/to/file1 path/to/file2 ...}}`

- Բացեք որոշակի հեռավոր ֆայլեր.:

`kate {{https://example.com/path/to/file1 https://example.com/path/to/file2 ...}}`

- Ստեղծեք խմբագրիչի նոր օրինակ, նույնիսկ եթե մեկն արդեն բաց է.:

`kate {{[-n|--new]}}`

- Բացեք ֆայլը կուրսորով կոնկրետ տողում.:

`kate {{[-l|--line]}} {{line_number}} {{path/to/file}}`

- Բացեք ֆայլ կուրսորով կոնկրետ տողում և սյունակում.:

`kate {{[-l|--line]}} {{line_number}} {{[-c|--column]}} {{column_number}} {{path/to/file}}`

- Ստեղծեք ֆայլ `stdin`-ից:

`cat {{path/to/file}} | kate {{[-i|--stdin]}}`

- Ցուցադրել օգնությունը.:

`kate {{[-h|--help]}}`
