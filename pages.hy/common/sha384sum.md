# sha384sum

> Հաշվարկել SHA384 ծածկագրային ստուգաչափերը:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>:.

- Հաշվեք SHA384 ստուգիչ գումարը մեկ կամ մի քանի ֆայլերի համար.:

`sha384sum {{path/to/file1 path/to/file2 ...}}`

- Հաշվեք և պահեք SHA384 ստուգիչ գումարների ցանկը ֆայլում.:

`sha384sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.sha384}}`

- Հաշվեք SHA384 ստուգիչ գումարը `stdin`-ից:

`{{command}} | sha384sum`

- Կարդացեք SHA384 ստուգիչ գումարների և ֆայլերի անունների ֆայլը և ստուգեք, որ բոլոր ֆայլերն ունեն համապատասխան ստուգման գումարներ.:

`sha384sum {{[-c|--check]}} {{path/to/file.sha384}}`

- Ցուցադրել հաղորդագրություն միայն բացակայող ֆայլերի համար կամ երբ ստուգումը ձախողվում է.:

`sha384sum {{[-c|--check]}} --quiet {{path/to/file.sha384}}`

- Ցուցադրել հաղորդագրություն միայն այն դեպքում, երբ ստուգումը ձախողվում է՝ անտեսելով բացակայող ֆայլերը.:

`sha384sum --ignore-missing {{[-c|--check]}} --quiet {{path/to/file.sha384}}`

- Ստուգեք ֆայլի հայտնի SHA384 ստուգիչ գումարը.:

`echo {{known_sha384_checksum_of_the_file}} {{path/to/file}} | sha384sum {{[-c|--check]}}`
