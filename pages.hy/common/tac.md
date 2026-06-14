# tac

> Ցուցադրել և միացնել ֆայլերը գծերով հակառակ հերթականությամբ:.
> Տես նաև՝ `cat`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/tac-invocation.html>:.

- Միացնել հատուկ ֆայլերը հակադարձ կարգով.:

`tac {{path/to/file1 path/to/file2 ...}}`

- Ցուցադրել `stdin`-ը հակառակ հերթականությամբ.:

`{{cat path/to/file}} | tac`

- Օգտագործեք հատուկ բաժանարար.:

`tac {{[-s|--separator]}} {{separator}} {{path/to/file1 path/to/file2 ...}}`

- Օգտագործեք որոշակի `regex` որպես բաժանարար՝:

`tac {{[-r|--regex]}} {{[-s|--separator]}} {{separator}} {{path/to/file1 path/to/file2 ...}}`

- Յուրաքանչյուր ֆայլից առաջ օգտագործեք բաժանարար.:

`tac {{[-b|--before]}} {{path/to/file1 path/to/file2 ...}}`
